from aiogram import types
from data_base import postgres_db
from .findface import find_face
from aiogram.types import File
from pathlib import Path
import shutil
import os
import re
from pydub import AudioSegment

class Handler:
	def __init__(self, bot):
		self.bot = bot

	async def command_start(self, message: types.Message):
		try:
			messages_id = message.from_user.id
			username = message.from_user.username
			await self.bot.send_message(messages_id, 'Hello ' + str(username))
			await self.bot.send_message(messages_id, "I'm bot send Audio Messages or Photo")
			await self.bot.send_message(messages_id, f'/help')
			await postgres_db.add_user(messages_id,username)

			await message.delete()
		except:
			await message.reply('add bot:\nhttps://t.me/PedictFootballBot')

	async def command_help(self, message: types.Message):
		await self.bot.send_message(message.from_user.id, f'/help\n/start')
		await message.delete()

	async def handle_file(self,file: File, file_name: str, path: str):
		Path(f"{path}").mkdir(parents=True, exist_ok=True)

		await self.bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")

	async def command_voice(self, message: types.Message):

		path = r'D:\face&audio_bot\voice' # directory  for audio messages
		path = os.path.join(path, str(message.from_user.id))
		def get_number_file(path): # last file number sorted by date
			if os.path.exists(path):
				dir_list = [os.path.join(path, x) for x in os.listdir(path)]
				if dir_list:
					date_list = [[x, os.path.getctime(x)] for x in dir_list]
					sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)
					a = sort_date_list[0][0]
					name_file = os.path.splitext(a)
					name_file = name_file[0].split('\\')[-1]
					n = re.findall('(\d+)', name_file)

					return int(n[0]) + 1
				else:
					return 0
			return 0
		n = get_number_file(path)

		voice = await message.voice.get_file()
		await self.handle_file(file=voice, file_name=f"{'audio_message_'+ str(n)}.wav", path=path) #{voice.file_id}
		sound = AudioSegment.from_file(os.path.join(path, f"{'audio_message_' + str(n)}.wav"))
		sound = sound.set_frame_rate(16000)
		sound.export(os.path.join(path, f"{'audio_message_' + str(n)}.wav"), format="wav")
		await self.bot.send_message(message.from_user.id, "audio is save")


	async def handle_photo(self, message: types.Message):
		file = await message.photo[-1].get_file()
		await message.photo[-1].download('file.jpg')
		name = file.file_path.split("/")[1]
		name = r'\{0}'.format(name)
		path1 = r'D:\face&audio_bot\file.jpg'
		path = r'D:\face&audio_bot\photos'  # create your directory for photo

		if len(find_face('file.jpg'))!=0:
			await self.bot.send_message(message.from_user.id, "Photo is save")
			shutil.copyfile(path1, path + name)
		else:
			await self.bot.send_message(message.from_user.id, "Photo is not save")
			await message.delete()

	async def echo(self, message: types.Message):
		await self.bot.send_message(message.from_user.id, "Only Audio Messages or Photo")
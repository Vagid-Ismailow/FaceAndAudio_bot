from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from aiogram.types import ContentType
import config
from handlers.client import Handler


def create_dispather():
    bot = Bot(token=config.TOKEN)
    handler = Handler(bot)

    dp = Dispatcher(bot)


    dp.register_message_handler(handler.command_start, commands=['start'])
    dp.register_message_handler(handler.command_help, commands=['help'])
    dp.register_message_handler(handler.command_voice, content_types=[ContentType.VOICE])
    dp.register_message_handler(handler.handle_photo, content_types=[ContentType.PHOTO])

    dp.register_message_handler(handler.echo)



    return dp
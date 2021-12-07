from aiogram.utils import executor
from data_base import entity


from create_bot import create_dispather
async def on_startup(_):
	await entity.main()



if __name__== '__main__':
	executor.start_polling(create_dispather(), skip_updates=True, on_startup=on_startup)
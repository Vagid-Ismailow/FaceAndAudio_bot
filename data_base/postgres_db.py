import asyncio
from .entity import Users

async def add_user(user_name, user_telegram_id):
    check = await Users.query.where(Users.name == user_name,
                            Users.user_telegram_id == user_telegram_id).gino.all()  # gino.first()
    if check is None:
        await Users.create(user_name=user_name, user_telegram_id=user_telegram_id)









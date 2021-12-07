from sqlalchemy import func
import asyncio
from gino import Gino
db = Gino()
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_telegram_id = db.Column(db.VARCHAR(200), nullable=False)



async def main():
    # await db.set_bind('postgresql://localhost/gino') # postgresql://postgres:1234@/db?host=127.0.0.1&port=5432
    await db.set_bind('postgresql://postgres:1234@/db?host=127.0.0.1&port=5432')
    print('connected')


    await db.gino.create_all()
    # await db.pop_bind().close()
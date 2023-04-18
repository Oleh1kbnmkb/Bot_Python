from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from config import PAYMENT_TOKEN
from main import dp, bot 
from shop import keyboard, cd 

import sqlite3

@dp.message_handler(Command('buy'))
async def buy_goods(message: Message):
    connect = sqlite3.connect('shop.db')
    cursor = connect.cursor()
    cursor.execute("""INSERT INTO users (user_id, name) VALUES (?, ?)""", [message.chat.id, message.chat.first_name])
    cursor.close()
    connect.commit()
    connect.close()

    await message.answer('Все добре')
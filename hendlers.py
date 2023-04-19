from config import Config
# from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.dispatcher.filters import Command
# from main import dp, bot
# from aiogram.utils.callback_data import CallbackData
# from hendlers import DataBase

import sqlite3



# cb = CallbackData('btn', 'type', 'id')
# db = DataBase('tgbot_database.db')




class DataBase:

    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    async def add_users(self, user_id, name):
        with self.connect:
            return self.cursor.execute("""INSERT INFO users (user_id, name, role) VALUES (?, ?, ?)""",
                                       [user_id, name, 'admin' if user_id == Config.admin_ids else 'user'])
        



async def get_products(self):
    with self.connect:
        return self.cursor.execute("""SELECT * FROM products""").fetchall()
    
async def get_user_product(self, product_id):
    with self.connect:
        return self.cursor.execute("""SELECT * FROM products WHERE product_id=(?)""", [product_id]).fetchall()
    
async def get_cart(self, user_id):
    with self.connect:
        return self.cursor.execute("""SELECT * FROM cart WHERE user_id=(?)""", [user_id]).fetchall()
    
async def add_to_cart(self, user_id, product_id):
    with self.connect:
        return self.cursor.execute("""INSERT INTO cart (user_id, product_id) VALUES (?, ?)""",
                                   [user_id, product_id])

async def empty_cart(self, user_id):
    with self.connect:
        return self.cursor.execute("""DELETE FROM cart WHERE user_id=(?)""", [user_id]).fetchall()
    


# @dp.message_handler(Command('shop'))
# async def shop(message: Message):
#     data = await db.get_products()
#     keyboard = InlineKeyboardMarkup()
#     for i in data:
#         keyboard.add(InlineKeyboardButton(text=f'{i[2]}: {i[3]}p', callback_data=f'btn:buy:{i[1]}'))
#     await message.answer('Що хочете придбати?', reply_markup=keyboard)
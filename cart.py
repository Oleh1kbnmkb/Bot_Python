from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.dispatcher.filters import Command
from main import dp, bot
from aiogram.utils.callback_data import CallbackData
from hendlers import DataBase


cb = CallbackData('btn', 'type', 'id')
db = DataBase('tgbot_database.db')




@dp.message_handler(commands=('shop'))
async def shop(message: Message):
    data = await db.get_products()
    keyboard = InlineKeyboardMarkup()
    for i in data:
        keyboard.add(InlineKeyboardButton(text=f'{i[2]}: {i[3]}p', callback_data=f'btn:buy:{i[1]}'))
    await message.answer('Що хочете придбати?', reply_markup=keyboard)


import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from site_url import computer

import os
from dotenv import load_dotenv
import markups as nav



load_dotenv()




TOKEN=os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)




@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, text ='Раді вітати вас у інтернет магазині Mabel Store.🎆🎇\nЦей бот допоможе вам вибрати товар за невеличким описом та з економить ваш час при виборі товару.😀', reply_markup=nav.BotMenu)







async def set_default_commands(dp):
     await bot.set_my_commands(
          [
          types.BotCommand('start', 'Запустити бота'),
          ]
     )





@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Магазин":
        await bot.send_message(message.from_user.id, text = "Оберіть категорію товару, який хочете придбати", reply_markup=nav.OtherMenu)
    elif message.text == "Офісні крісла":
        await bot.send_message(message.from_user.id, text = "Офісні крісла", reply_markup=nav.goods)
    elif message.text == "Головне меню":
        await bot.send_message(message.from_user.id, text = "Головне меню", reply_markup=nav.BotMenu)
    elif message.text == "Дивани":
        await bot.send_message(message.from_user.id, text = "Дивани", reply_markup=nav.sofas)
    elif message.text == "Робочі столи":
        await bot.send_message(message.from_user.id, text = "Робочі столи", reply_markup=nav.table_school)
    elif message.text == "Журнальні столи":
        await bot.send_message(message.from_user.id, text = "Журнальні столи", reply_markup=nav.magazine_tables)
    elif message.text == "Полиці для книг":
          await bot.send_message(message.from_user.id, text = "Полиці для книг", reply_markup=nav.book_shelves)

          computer_shop = InlineKeyboardMarkup()
          for teh in computer_shop:
                button = InlineKeyboardButton(text = computer, callback_data=computer)
                computer_shop.add(button)


          

         
@dp.callback_query_handler()
async def computer_info_handler(callback_query: types.CallbackQuery):
     if callback_query.data in computer.keys():
          computer_name = computer[callback_query.data]["name"]
          url = computer[callback_query.data]["site_url"]
          computer_description = computer[callback_query.data]["description"]
          computer_price = computer[callback_query.data]["price"]
          message = f"<b>Назва: </b> {computer_name}\n<b>Посилання на магазин: </b> {url}\n\n<b>Опис: </b> {computer_description}\n\n<b>Ціна:</b> {computer_price}"
          await bot.send_message(callback_query.message.chat.id, message, parse_mode='html')
     else:
          await bot.send_message(callback_query.message.chat.id, "Такого товару нажаль немає в наявності😟")








async def on_startup(dp):
     await set_default_commands(dp)

  
  
if __name__ == '__main__':
     executor.start_polling(dp)
    
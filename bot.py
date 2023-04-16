import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from site_url import computer
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config



logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.Token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, text ='Раді вітати вас у інтернет магазині Rozetka!\nЦей бот допоможе вам придбати товар швидко і безпечно.', reply_markup=nav.BotMenu)


     









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
    elif message.text == "Крісло АКЛАС Гілмор":
          await bot.send_message(message.from_user.id, text = "")
    
          computer_shop = InlineKeyboardMarkup()
          for teh in computer_shop:
            button = InlineKeyboardButton(text = computer, callback_data=computer)
            computer_shop.add(button)
          

         
   

@dp.callback_query_handler()
async def computer_info_handler(callback_query: types.CallbackQuery):
     if callback_query.data in computer.keys():
          await bot.send_photo(callback_query.message.chat.id, computer[callback_query.data]["photo"])
          computer_price = computer[callback_query.data]["price"]
          message = f"<b>Price: </b> {computer_price}"
          await bot.send_message(callback_query.message.chat.id, message, parse_mode='html')
     else:
          await bot.send_message(callback_query.message.chat.id, "Такого товару нажаль немає в наявності😟")
          









  
  
if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)
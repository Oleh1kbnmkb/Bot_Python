import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from site_url import furniture


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
    await bot.send_message(message.from_user.id, text ='Раді вітати вас у інтернет магазині City Store.🎆🎇\nЦей бот допоможе вам вибрати товар за невеличким описом та з економить ваш час при виборі товару.😀', reply_markup=nav.BotMenu)







async def set_default_commands(dp):
     await bot.set_my_commands(
          [
          types.BotCommand('start', 'Запустити бота'),
          ]
     )





@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Магазин":
        await bot.send_message(message.from_user.id, text = "Оберіть категорію товару, який хочете придбати", reply_markup=nav.OtherMenu1)
    elif message.text == "Меблі":
         await bot.send_message(message.from_user.id, text = "Меблі", reply_markup=nav.OtherMenu)
    elif message.text == "Назад":
         await bot.send_message(message.from_user.id, text = "Назад", reply_markup=nav.OtherMenu1)
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
    elif message.text == "Шафи купе":
          await bot.send_message(message.from_user.id, text = "Шафи купе", reply_markup=nav.cabinet)
    elif message.text == "Комп'ютерна техніка":
          await bot.send_message(message.from_user.id, text="Комп'ютерна техніка", reply_markup=nav.LaptopMenu)
    elif message.text == "Ноутбуки":
          await bot.send_message(message.from_user.id, text="Ноутбуки", reply_markup=nav.laptop1)
    elif message.text == "Назад":
          await bot.send_message(message.from_user.id, text="Назад", reply_markup=nav.OtherMenu1)
    elif message.text == "Комп'ютери":
          await bot.send_message(message.from_user.id, text="Комп'ютери", reply_markup=nav.computers)
    elif message.text == "Телевізори":
          await bot.send_message(message.from_user.id, text="Телевізори", reply_markup=nav.tv_menu)
    elif message.text == "Офіс, школа книги":
          await bot.send_message(message.from_user.id, text="Офіс, школа книги", reply_markup=nav.SchoolMenu)
    elif message.text == "Рюкзаки":
          await bot.send_message(message.from_user.id, text="Рюкзаки", reply_markup=nav.back2)
    elif message.text == "Шкільне приладдя":
          await bot.send_message(message.from_user.id, text="Шкільне приладдя", reply_markup=nav.school_ba)
    elif message.text == "Паперова продукція":
          await bot.send_message(message.from_user.id, text="Паперова продукція", reply_markup=nav.paper1)
    elif message.text == "Зоотовари":
          await bot.send_message(message.from_user.id, text="Зоотовари", reply_markup=nav.PetMenu)
    elif message.text == "Собака":
          await bot.send_message(message.from_user.id, text="Собака", reply_markup=nav.goods_dog)
    elif message.text == "Кіт":
          await bot.send_message(message.from_user.id, text="Кіт", reply_markup=nav.goods_cat)
    elif message.text == "Побутова техніка":
          await bot.send_message(message.from_user.id, text="Побутова техніка", reply_markup=nav.houseMenu)
    elif message.text == "Холодильники":
          await bot.send_message(message.from_user.id, text="Холодильники", reply_markup=nav.cold1)
    elif message.text == "Роботи пилососи":
          await bot.send_message(message.from_user.id, text="Роботи пилососи", reply_markup=nav.clear1)
    elif message.text == "Пральні машини":
          await bot.send_message(message.from_user.id, text="Пральні машини", reply_markup=nav.car6)
    elif message.text == "Рюкзаки":
          await bot.send_message(message.from_user.id, text="Рюкзаки", reply_markup=nav.back2)
    elif message.text == "Шкільне приладдя":
          await bot.send_message(message.from_user.id, text="Шкільне приладдя", reply_markup=nav.school_ba)
    elif message.text == "Паперова продукція":
          await bot.send_message(message.from_user.id, text="Паперова продукція", reply_markup=nav.paper1)


          furniture_shop = InlineKeyboardMarkup()
          for fur in furniture_shop:
              button = InlineKeyboardButton(text = furniture, callback_data=furniture)
              furniture_shop.add(button)


        





         


          

         
@dp.callback_query_handler()
async def furniture_info_handler(callback_query: types.CallbackQuery):
     if callback_query.data in furniture.keys():
          await bot.send_photo(callback_query.message.chat.id, furniture[callback_query.data]["photo"])
          furniture_name = furniture[callback_query.data]["name"]
          url = furniture[callback_query.data]["site_url"]
          furniture_description = furniture[callback_query.data]["description"]
          furniture_price = furniture[callback_query.data]["price"]
          message = f"<b>Назва: </b> {furniture_name}\n<b>Посилання на магазин: </b> {url}\n\n<b>Опис: </b> {furniture_description}\n\n<b>Ціна:</b> {furniture_price}"
          await bot.send_message(callback_query.message.chat.id, message, parse_mode='html')
     else:
          await bot.send_message(callback_query.message.chat.id, "Такого товару нажаль немає в наявності😟")











async def on_startup(dp):
     await set_default_commands(dp)

  
  
if __name__ == '__main__':
     executor.start_polling(dp, on_startup=on_startup)
    
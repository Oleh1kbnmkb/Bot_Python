import logging
from aiogram import Bot, Dispatcher, executor, types

from site_url import computer
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from hendlers import dp

# from aiogram.types import Message, CallbackQuery
# from aiogram.dispatcher.filters import Command
# from config import PAYMENT_TOKEN
# from main import Dispatcher
# from shop import keyboard, cd

# import sqlite3




TOKEN = "6255018670:AAHDRCHL72HP0STq6oHn2WmWv6YcNtQtwoc"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, text ='Раді вітати вас у інтернет магазині Rozetka!\nЦей бот допоможе вам придбати товар швидко і безпечно.', reply_markup=BotMenu)






btnMenu = KeyboardButton("Головне меню")

# --- Bot Menu ---
shop_choice = ReplyKeyboardMarkup()
btn1 = KeyboardButton("Магазин")
btn2 = KeyboardButton("Корзина")
btn3 = KeyboardButton("Перейти до оформлення замовлення")
BotMenu = ReplyKeyboardMarkup(resize_keyboard=True)
BotMenu.add(btn1, btn2)
BotMenu.add(btn3)



# --- Bot Other Menu ---
shop_goods = ReplyKeyboardMarkup()
technique = KeyboardButton("Офісні крісла")
technique1 = KeyboardButton("Дивани")
home_appliances = KeyboardButton("Робочі столи")
home_goods = KeyboardButton("Журнальні столи")
instruments = KeyboardButton("Полиці для книг")



OtherMenu = ReplyKeyboardMarkup(resize_keyboard=True)
OtherMenu.add(technique, technique1)
OtherMenu.add(home_appliances, home_goods) 
OtherMenu.add(instruments, btnMenu)







# --- Laptop Menu ---
goods = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Крісло АКЛАС Гілмор", callback_data="Крісло АКЛАС Гілмор")],
    [InlineKeyboardButton(text = "НКрісло АКЛАС Сіті", callback_data="Крісло АКЛАС Сіті")],
    [InlineKeyboardButton(text = "Крісло АКЛАС Арсі", callback_data="Крісло АКЛАС Арсі")],
    [InlineKeyboardButton(text = "Крісло конференційне АКЛАС Ларк", callback_data="Крісло конференційне АКЛАС Ларк")],
    [InlineKeyboardButton(text = "Крісло АКЛАС Тета", callback_data="Крісло АКЛАС Тета")]
    ]
)


sofas = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Диван Embawood Луна", callback_data="Диван Embawood Луна")],
    [InlineKeyboardButton(text = "Диван DLS Колібрі-3-КС", callback_data="Диван DLS Колібрі-3-КС")],
    [InlineKeyboardButton(text = "Диван модульний RICHMAN ", callback_data="Диван модульний RICHMAN ")],
    [InlineKeyboardButton(text = "Диван модульний", callback_data="Диван модульний")],
    [InlineKeyboardButton(text = "Диван DANIRO Лірик", callback_data="Диван DANIRO Лірик")]
    ]
)



table_school = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Стіл M-Concept Серія Джет", callback_data="Стіл M-Concept Серія Джет")],
    [InlineKeyboardButton(text = "Стіл M-Concept Серія Атрибут", callback_data="Стіл M-Concept Серія Атрибут")],
    [InlineKeyboardButton(text = "Стіл M-Concept Серія Сенс", callback_data="Стіл M-Concept Серія Сенс")],
    [InlineKeyboardButton(text = "Стіл комп'ютерний СК-3 Kredens furniture", callback_data="Стіл комп'ютерний СК-3 Kredens furniture")],
    [InlineKeyboardButton(text = "Стіл Бянко (графіт)", callback_data="Стіл Бянко (графіт)")]
    ]
)



magazine_tables = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Столик журнальний Wudus Plump", callback_data="Столик журнальний Wudus Plump")],
    [InlineKeyboardButton(text = "Столик журнальний ЧФЛИ Марс", callback_data="Столик журнальний ЧФЛИ Марс")],
    [InlineKeyboardButton(text = "Стіл журнальний M-Concept", callback_data="Стіл журнальний M-Concept")],
    [InlineKeyboardButton(text = "Стіл журнальний Антонік", callback_data="Стіл журнальний Антонік")],
    [InlineKeyboardButton(text = "Стіл журнальний Антонік ДС-2", callback_data="Стіл журнальний Антонік ДС-2")]
    ]
)


book_shelves = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Полка П-27-53", callback_data="Полка П-27-53")],
    [InlineKeyboardButton(text = "Книжкова полиця ПК-2", callback_data="Книжкова полиця ПК-2")],
    [InlineKeyboardButton(text = "Полка декоративная DC ДС-4", callback_data="Полка декоративная DC ДС-4")],
    [InlineKeyboardButton(text = "Полиця навісна на стіну П-1", callback_data="Полиця навісна на стіну П-1")],
    [InlineKeyboardButton(text = "Полка Forte Erika для книг", callback_data="Полка Forte Erika для книг")]
    ]
)





     

     
async def set_default_commands(dp):
     await bot.set_my_commands(
          [
          types.BotCommand('start', 'Запустити бота'),
          types.BotCommand('buy', 'Купити товар з магазину')
          ]
     )





@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "Магазин":
        await bot.send_message(message.from_user.id, text = "Оберіть категорію товару, який хочете придбати", reply_markup=OtherMenu)
    elif message.text == "Офісні крісла":
          await bot.send_message(message.from_user.id, text = "Офісні крісла", reply_markup=goods)
    elif message.text == "Головне меню":
          await bot.send_message(message.from_user.id, text = "Головне меню", reply_markup=BotMenu)
    elif message.text == "Дивани":
          await bot.send_message(message.from_user.id, text = "Дивани", reply_markup=sofas)
    elif message.text == "Робочі столи":
          await bot.send_message(message.from_user.id, text = "Робочі столи", reply_markup=table_school)
    elif message.text == "Журнальні столи":
          await bot.send_message(message.from_user.id, text = "Журнальні столи", reply_markup=magazine_tables)
    elif message.text == "Полиці для книг":
          await bot.send_message(message.from_user.id, text = "Полиці для книг", reply_markup=book_shelves)
    
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
          keyboard3 = types.InlineKeyboardMarkup()
          button = types.InlineKeyboardButton(text = 'Добавити товар у корзину', callback_data='Добавити товар у корзину')
          await bot.send_message(callback_query.message.chat.id, message, parse_mode='html')
     else:
          await bot.send_message(callback_query.message.chat.id, "Такого товару нажаль немає в наявності😟")



# @dp.message_handler(commands=['buy'])
# async def buy(message: Message):
#      connect = sqlite3.connect('shop.db')
#      cursor = connect.cursor()
#      cursor.execute("""INSERT INTO users (user_id, name) VALUES (?, ?)""", [message.chat.id, message.chat.first_name])
#      cursor.close()
#      connect.commit()
#      connect.close()
#      await message.answer('Бот готовий')

# @dp.message_handler(commands=['cart'])
# async def cart(message: Message):
#      await message.answer('Виберіть, що хочете купити', reply_markup=keyboard)


# @dp.callback_query_handler(cd.filter(id = '1'))
# async def smart(call: CallbackQuery, callback_data: dict):
#      await call.answer(callback_time = 10)

#      product_id = callback_data.get('id')
#      user_id = call.message.chat.id

#      connect = sqlite3.connect('shop.db')
#      cursor = connect.cursor()
#      cursor.execute("""INSERT INTO users (user_id, name) VALUES (?, ?)""", [user_id, product_id])
#      cursor.close()
#      connect.commit()
#      connect.close()

#      await call.message.answer('Товар додано в корзину')










async def on_startup(dp):
     await set_default_commands(dp)

  
  
if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)
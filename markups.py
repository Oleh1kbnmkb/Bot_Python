from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from site_url import computer



btnMenu = KeyboardButton("Головне меню")

# --- Bot Menu ---
shop_choice = ReplyKeyboardMarkup()
btn1 = KeyboardButton("Магазин")
btn2 = KeyboardButton("Корзина")
btn3 = KeyboardButton("Перейти до оформлення замовлення")
BotMenu = ReplyKeyboardMarkup(resize_keyboard=True)
BotMenu.add(btn1, btn2)
BotMenu.add(btn3)



# back = KeyboardButton(text = "Назад")

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


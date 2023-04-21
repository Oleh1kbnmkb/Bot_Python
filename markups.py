from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton




btnMenu = KeyboardButton("Головне меню")

# --- Bot Menu ---
shop_choice = ReplyKeyboardMarkup()
btn1 = KeyboardButton("Магазин")
BotMenu = ReplyKeyboardMarkup(resize_keyboard=True)
BotMenu.add(btn1)

back5 = KeyboardButton("Назад")

# --- Bot Other Menu 1 ---
shop_goods1 = ReplyKeyboardMarkup()
fur = KeyboardButton("Меблі")
teh = KeyboardButton("Комп'ютерна техніка")
tv = KeyboardButton("Телевізори")
backpacks = KeyboardButton("Офіс, школа книги")
pet_products = KeyboardButton("Зоотовари")
household = KeyboardButton("Побутова техніка")
OtherMenu1 = ReplyKeyboardMarkup(resize_keyboard=True)
OtherMenu1.add(teh, tv, fur)
OtherMenu1.add(household, pet_products, backpacks)
OtherMenu1.add(btnMenu)



# --- backpacks ----
backpacks1 = ReplyKeyboardMarkup()
back1 = KeyboardButton("Рюкзаки")
school_b = KeyboardButton("Шкільне приладдя")
paper = KeyboardButton("Паперова продукція")
SchoolMenu = ReplyKeyboardMarkup(resize_keyboard=True)
SchoolMenu.add(back1, school_b)
SchoolMenu.add(paper, back5)




# --- pet_products ----
pet_products1 = ReplyKeyboardMarkup()
dog = KeyboardButton("Собака")
cat = KeyboardButton("Кіт")
PetMenu = ReplyKeyboardMarkup()
PetMenu.add(dog, cat)
PetMenu.add(back5)





# --- household ---
household1 = ReplyKeyboardMarkup()
cold = KeyboardButton("Холодильники")
clear = KeyboardButton("Роботи пилососи")
car = KeyboardButton("Пральні машини")
houseMenu = ReplyKeyboardMarkup()
houseMenu.add(cold, clear)
houseMenu.add(car, back5)






laptop = ReplyKeyboardMarkup()
lap = KeyboardButton("Ноутбуки")
comp = KeyboardButton("Комп'ютери")
LaptopMenu = ReplyKeyboardMarkup(resize_keyboard=True)
LaptopMenu.add(lap, comp)
LaptopMenu.add(back5)





back = KeyboardButton(text = "Назад")

# --- Bot Other Menu ---
shop_goods = ReplyKeyboardMarkup()
technique = KeyboardButton("Офісні крісла")
technique1 = KeyboardButton("Дивани")
home_appliances = KeyboardButton("Робочі столи")
home_goods = KeyboardButton("Журнальні столи")
instruments = KeyboardButton("Полиці для книг")
cabinet1 = KeyboardButton("Шафи купе")
OtherMenu = ReplyKeyboardMarkup(resize_keyboard=True)
OtherMenu.add(technique, technique1)
OtherMenu.add(home_appliances, home_goods) 
OtherMenu.add(instruments, cabinet1)
OtherMenu.add(back)






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
    [InlineKeyboardButton(text = "Стіл журнальний Антонік Шарм", callback_data="Стіл журнальний Антонік Шарм")],
    [InlineKeyboardButton(text = "Стіл журнальний Антонік ДС-21", callback_data="Стіл журнальний Антонік ДС-21")]
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


cabinet = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Шафа купе ДІМ В-104", callback_data="Шафа купе ДІМ В-104")],
    [InlineKeyboardButton(text = "Шафа купе ДІМ В-146", callback_data="Шафа купе ДІМ В-146")],
    [InlineKeyboardButton(text = "Шафа купе ДІМ ВН-486", callback_data="Шафа купе ДІМ ВН-486")],
    [InlineKeyboardButton(text = "Шафа купе ДІМ В-106", callback_data="Шафа купе ДІМ В-106")],
    [InlineKeyboardButton(text = "Шафа купе ДІМ Камелот КН 25", callback_data="Шафа купе ДІМ Камелот КН 25")]
    ]
)


laptop1 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Ноутбук Acer Aspire 5 ", callback_data="Ноутбук Acer Aspire 5 ")],
    [InlineKeyboardButton(text = "Ноутбук Lenovo IdeaPad L3", callback_data="Ноутбук Lenovo IdeaPad L3")],
    [InlineKeyboardButton(text = "Ноутбук Apple MacBook Air 13", callback_data="Ноутбук Apple MacBook Air 13")],
    [InlineKeyboardButton(text = "Ноутбук ASUS Vivobook 16X", callback_data="Ноутбук ASUS Vivobook 16X")],
    [InlineKeyboardButton(text = "Ноутбук HP Laptop 15s", callback_data="Ноутбук HP Laptop 15s")]
    ]
)



computers = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Комп'ютер Asus S500MC", callback_data="Комп'ютер Asus S500MC")],
    [InlineKeyboardButton(text = "Комп'ютер Cobra Optimal", callback_data="Комп'ютер Cobra Optimal")],
    [InlineKeyboardButton(text = "Ігровий Athlon X4 970", callback_data="Ігровий Athlon X4 970")],
    [InlineKeyboardButton(text = "Комп'ютер Apple Mac Studio M1", callback_data="Комп'ютер Apple Mac Studio M1")],
    [InlineKeyboardButton(text = "Комп'ютер ARTLINE Gaming X47", callback_data="Комп'ютер ARTLINE Gaming X47")]
    ]
)


tv_menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Телевізор Samsung UE50", callback_data="Телевізор Samsung UE50")],
    [InlineKeyboardButton(text = "Телевизор LG 55", callback_data="Телевизор LG 55")],
    [InlineKeyboardButton(text = "Телевизор LG 32L", callback_data="Телевизор LG 32L")],
    [InlineKeyboardButton(text = "Телевизор SETUP 24", callback_data="Телевизор SETUP 24")],
    [InlineKeyboardButton(text = "Телевизор Ergo 43G", callback_data="Телевизор Ergo 43G")],
    [InlineKeyboardButton(text = "Телевизор Nokia Smart TV", callback_data="Телевизор Nokia Smart TV")]
    ]
)

goods_dog = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Корми для собак", callback_data="Корми для собак")],
    [InlineKeyboardButton(text = "Посуд для собак", callback_data="Посуд для собак")],
    [InlineKeyboardButton(text = "Одяг для собак", callback_data="Одяг для собак")],
    [InlineKeyboardButton(text = "Іграшки для собак", callback_data="Іграшки для собак")],
    [InlineKeyboardButton(text = "Спальні місця для собак", callback_data="Спальні місця для собак")]
    ]
)


goods_cat = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Корми для котів", callback_data="Корми для котів")],
    [InlineKeyboardButton(text = "Посуд для котів", callback_data="Посуд для котів")],
    [InlineKeyboardButton(text = "Наповнювачі для котів", callback_data="Наповнювачі для котів")],
    [InlineKeyboardButton(text = "Іграшки для котів", callback_data="Іграшки для котів")],
    [InlineKeyboardButton(text = "Спальні місця для котів", callback_data="Спальні місця для котів")]
    ]
)



cold1 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Холодильник SAMSUNG RB38", callback_data="Холодильник SAMSUNG RB38")],
    [InlineKeyboardButton(text = "Холодильник BOSCH KGN36", callback_data="Холодильник BOSCH KGN36")],
    [InlineKeyboardButton(text = "Холодильник Whirlpool W7X", callback_data="Холодильник Whirlpool W7X")],
    [InlineKeyboardButton(text = "Холодильник BEKO RCNA40", callback_data="Холодильник BEKO RCNA40")],
    [InlineKeyboardButton(text = "Холодильник GORENJE RK62", callback_data="Холодильник GORENJE RK62")]
    ]
)



clear1 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Робот-пылесос Rowenta X-PLORER", callback_data="Робот-пылесос Rowenta X-PLORER")],
    [InlineKeyboardButton(text = "Робот-пилосос Rowenta X-PLORER S130AI", callback_data="Робот-пилосос Rowenta X-PLORER S130AI")],
    [InlineKeyboardButton(text = "Робот-пилосос Roborock Vacuum Cleaner", callback_data="Робот-пилосос Roborock Vacuum Cleaner")],
    [InlineKeyboardButton(text = "Робот-пилосос ECOVACS DEEBOT OZMO", callback_data="Робот-пилосос ECOVACS DEEBOT OZMO")],
    [InlineKeyboardButton(text = "Робот-пилосос ECOVACS Deebot OZMO T8 AIVI", callback_data="Робот-пилосос ECOVACS Deebot OZMO T8 AIVI")]
    ]
)


car6 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Пральна машина вузька WHIRLPOOL", callback_data="Пральна машина вузька WHIRLPOOL")],
    [InlineKeyboardButton(text = "Пральна машина вузька SAMSUNG ", callback_data="Пральна машина вузька SAMSUNG ")],
    [InlineKeyboardButton(text = "Пральна машина вузька INDESIT ", callback_data="Пральна машина вузька INDESIT")]
    ]
)


back2 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Рюкзаки для дівчат", callback_data="Рюкзаки для дівчат")],
    [InlineKeyboardButton(text = "Рюкзаки для хлопців", callback_data="Рюкзаки для хлопців")],
    
    ]
)



school_ba = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Пенали", callback_data="Пенали")],
    [InlineKeyboardButton(text = "Зошити", callback_data="Зошити")],
    [InlineKeyboardButton(text = "Фломастери", callback_data="Фломастери")],
    [InlineKeyboardButton(text = "Щоденники", callback_data="Щоденники")],
    [InlineKeyboardButton(text = "Пластилін", callback_data="Пластилін")],
    [InlineKeyboardButton(text = "Альбоми для малювання", callback_data="Альбоми для малювання")]
    ]
)


paper1 = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text = "Папір офісний", callback_data="Папір офісний")],
    [InlineKeyboardButton(text = "Блокноти, зошити офісні", callback_data="Блокноти, зошити офісні")],
    [InlineKeyboardButton(text = "Календарі", callback_data="Календарі")],
    [InlineKeyboardButton(text = "Папір для нотаток", callback_data="Папір для нотаток")],
    [InlineKeyboardButton(text = "Кольоровий папір", callback_data="Кольоровий папір")],
    [InlineKeyboardButton(text = "Папір спеціальний", callback_data="Папір спеціальний")]
    ]
)
from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    username = State()
    email = State()
    password = State()
    year = State()
    balance = State()
    is_admin = State()
    check = State()


class Login(StatesGroup):
    username = State()
    password = State()


class Add_product(StatesGroup):
    product_name = State()
    product_price = State()
    product_amount = State()
    check = State()


class show_one_product1(StatesGroup):
    product_id = State()


class show_add_product2(StatesGroup):
    product1_id = State()

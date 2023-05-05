from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db_con import con, cur


def register():
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton("Register", callback_data="register"),
            InlineKeyboardButton("Login", callback_data="login")
            )
    return ikm


def menu():
    ikm = InlineKeyboardMarkup(row_width=1)
    ikm.add(InlineKeyboardButton("1) Buy products", callback_data="buy_product"),
            InlineKeyboardButton("2) Check balance", callback_data="check_balance"),
            InlineKeyboardButton("3) History", callback_data="history"),
            InlineKeyboardButton("4) Exit", callback_data="exit")
            )
    return ikm


def order_menu(username: str):
    ikm = InlineKeyboardMarkup(row_width=1)
    ikm.add(InlineKeyboardButton("1) Show all products", callback_data="shw_" + f"{username}"),
            InlineKeyboardButton("2) Show one product", callback_data="show_one"),
            InlineKeyboardButton("3) My added products", callback_data="ma_" + f"{username}"),
            InlineKeyboardButton("4) Add product", callback_data="adp_" + f'{username}'),
            InlineKeyboardButton("5) Remove product", callback_data="rem_p" + f"{username}"),
            InlineKeyboardButton("6) Change product", callback_data="change_product"),
            InlineKeyboardButton("7) All reports", callback_data="all_reports"),
            InlineKeyboardButton("8) Send all reports", callback_data="send_reports"),
            InlineKeyboardButton("9) Exit", callback_data="exit")
            )
    return ikm


def back():
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton("Yes", callback_data='yes'),
            InlineKeyboardButton("No", callback_data='no'))
    return ikm


def data(username: str) -> bool:
    query = 'select  username from users where username=%s '
    cur.execute(query, (username,))
    return cur.fetchone()


def data_1(username: str, password: str) -> bool:
    query = 'select username from users where username=%s and password=%s'
    cur.execute(query, (username, password))
    return cur.fetchone()


def _is_admin(username: str) -> bool:  # noqa
    query = 'select * from users where username = %s'  # noqa
    cur.execute(query, (username,))
    admin = cur.fetchone()
    return admin and admin[7] == True


def show_all_product() -> tuple:
    query = 'select * from product'
    cur.execute(query)
    return cur.fetchall()


def admin_id(username: str):
    query = 'select id from users where username = %s'  # noqa
    cur.execute(query, (username,))
    id_create = cur.fetchone()
    return id_create


def show_one_product(id: int):
    query = 'select * from product where id = %s'  # noqa
    cur.execute(query, (id,))
    return cur.fetchall()


def show_my_add_product(id_create: int):
    query = 'select * from product where admin_id = %s'  # noqa
    cur.execute(query, (id_create,))
    product = cur.fetchall()
    l = []
    if product:
        for i in product:
            l.append(i)
        return l
    else:
        return False


def check_product_id(id: int, id_create: int):  # noqa
    query = 'select * from product where id = %s and admin_id = %s'  # noqa
    cur.execute(query, (id, id_create))
    return cur.fetchone()


def remove_product(id: int, id_create: int):  # noqa
    if check_product_id(id, id_create):
        query = 'delete from product where id = %s and admin_id = %s'  # noqa
        cur.execute(query, (id, id_create))
        con.commit()
        return ('Product has been removed!!!')
    else:
        return ('No such id exists')

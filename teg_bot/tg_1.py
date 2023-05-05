import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from aiogram.utils import executor, callback_data
import aiogram.utils.markdown as md
from teg_bot.dispatcher_1 import dp
from teg_bot.func_1 import register, back, menu
from teg_bot.state_1 import Form, Login, Add_product, show_one_product1
from db_con import con, cur
from func_1 import data, data_1, _is_admin, order_menu, admin_id, show_all_product, show_one_product, \
    show_my_add_product,check_product_id,remove_product



@dp.message_handler(commands=["start"])
async def start_handler(message: Message):
    await message.answer("Welcome to my first telegram bot ", reply_markup=register())


@dp.callback_query_handler(Text("register"))
async def register_hand(callback: CallbackQuery):
    await callback.message.delete()
    await Form.name.set()
    await callback.message.answer("Enter your name  :")



@dp.message_handler(state=Form.name)
async def ans_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await Form.next()
    await message.answer("Enter your useranme  :")


@dp.message_handler(state=Form.username)
async def ans_username(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await Form.next()
    await message.answer("Enter your email  :")


@dp.message_handler(state=Form.email)
async def ans_password(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await Form.next()
    await message.answer("Enter your  password :")


@dp.message_handler(state=Form.password)
async def ans_year(message: Message, state=FSMContext):
    await state.update_data(password=message.text)
    await Form.next()
    await message.answer("Enter your year  :")


@dp.message_handler(state=Form.year)
async def ans_balance(message: Message, state=FSMContext):
    await state.update_data(year=message.text)
    await Form.next()
    await message.answer("Enter balance  :")


@dp.message_handler(state=Form.balance)
async def ans_admin(message: Message, state=FSMContext):
    await state.update_data(balance=message.text)
    await Form.next()
    await message.answer("Is admin  :")


@dp.message_handler(state=Form.is_admin)
async def ans_email(message: Message, state: FSMContext):
    await state.update_data(is_admin=message.text)
    async with state.proxy() as f:
        text = md.text(
            md.text(md.bold("Your name  :"), f['name']),
            md.text(md.bold("Your username  :"), f['username']),
            md.text(md.bold("Your email  :"), f['email']),
            md.text(md.bold("Your password  :"), f['password']),
            md.text(md.bold("Your year  :"), f['year']),
            md.text(md.bold("Your balance  :"), f['balance']),
            md.text(md.bold("Is_admin  :"), f['is_admin']),

            sep='\n'
        )

    await Form.next()
    await message.answer('Is your enter informations are correct?\n' + text, parse_mode=ParseMode.MARKDOWN,
                         reply_markup=back())


@dp.callback_query_handler(Text(['yes', 'no']), state=Form.check)
async def ans_yes(callback: CallbackQuery, state: FSMContext):
    print(callback.data)
    async with state.proxy() as f:
        if callback.data == 'yes':
            text = "insert into users(name, username, email, password, year, balance,  is_admin) values (%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(text,
                        (f['name'], f['username'], f['email'], f['password'], f['year'], f['balance'], f['is_admin']))
            con.commit()
        else:
            await callback.message.answer("Try again  :", reply_markup=register())


@dp.callback_query_handler(Text("login"))
async def register_hand(callback: CallbackQuery):
    await callback.message.delete()
    await Login.username.set()
    await callback.message.answer("Enter your username  :")


@dp.message_handler(state=Login.username)
async def log_1(message: Message, state=FSMContext):
    await state.update_data(username=message.text)
    if data(message.text):
        await Login.next()
        await message.answer("Enter your password  :")
    else:
        await message.answer("Invalid user`")


@dp.message_handler(state=Login.password)
async def ans_email(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    async with state.proxy() as f:
        if data_1(f['username'], message.text):
            await message.answer("Succesful entry")
            if _is_admin(f['username']):
                await message.answer("Admin of menu", reply_markup=order_menu(f['username']))
            else:
                await message.answer("Customer of menu", reply_markup=menu())
        else:
            await message.answer("Wrong")
    await state.finish()


@dp.callback_query_handler(lambda callback: 'adp_' in callback.data)
async def add_product_hands(callback: CallbackQuery, state: FSMContext):
    username = callback.data.lstrip('adp_')
    await state.update_data(username=username)
    await callback.message.delete()
    await Add_product.product_name.set()
    await callback.message.answer("Enter product name  :")


@dp.message_handler(state=Add_product.product_name)
async def ans_name(message: Message, state: FSMContext):
    await state.update_data(product_name=message.text)
    await Add_product.next()
    await message.answer("Enter product price  :")


@dp.message_handler(state=Add_product.product_price)
async def ans_name(message: Message, state: FSMContext):
    await state.update_data(product_price=message.text)
    await Add_product.next()
    await message.answer("Enter product amount  :")


@dp.message_handler(state=Add_product.product_amount)
async def ans_email(message: Message, state: FSMContext):
    await state.update_data(product_amount=message.text)
    async with state.proxy() as f:
        text = md.text(
            md.text(md.bold("Product name  :"), f['product_name']),
            md.text(md.bold("Product price :"), f['product_price']),
            md.text(md.bold("Product amount  :"), f['product_amount']),
            sep='\n'
        )

    await Add_product.next()
    await message.answer('Is your enter informations are correct?\n' + text, parse_mode=ParseMode.MARKDOWN,
                         reply_markup=back())


@dp.callback_query_handler(lambda callback: 'yes' or 'no' in callback.data, state=Add_product.check)
async def ans_yes(callback: CallbackQuery, state: FSMContext):
    print(callback.data)
    async with state.proxy() as f:
        pk = admin_id(f['username'])
        if callback.data == 'yes':
            text = "insert into product(admin_id,name,price, amount) values (%s,%s,%s,%s)"
            cur.execute(text,
                        (pk, f['product_name'], f['product_price'], f['product_amount']))
            con.commit()
            await state.finish()
        else:
            await callback.message.answer("Try again  :")
        await state.finish()


@dp.callback_query_handler(lambda callback: 'shw_' in callback.data)
async def register_hand(callback: CallbackQuery):
    await callback.message.delete()
    prod1 = show_all_product()
    l = ''
    for i in prod1:
        l += ''.join(f'Product name  :{i[2]} \n Product price  :{i[3]} \n Product amount  :{i[4]}')
    await callback.message.answer(f'All products  :' + '\n' + f"{l}")


@dp.callback_query_handler(Text("show_one"))
async def show_one(callback: CallbackQuery):
    await show_one_product1.product_id.set()
    await callback.message.answer("Enter product id  :")


@dp.message_handler(state=show_one_product1.product_id)
async def show_one_1(message: Message, state=FSMContext):
    await state.update_data(product_id=message.text)
    async with state.proxy() as f:
        prod2 = show_one_product(message.text)
        l = ''
        for i in prod2:
            l += ''.join(f'Product name  :{i[2]} \n Product price  :{i[3]} \n Product amount  :{i[4]}')
        await message.answer(f'Show one product  :' + '\n' + f"{l}")
    await state.finish()


@dp.callback_query_handler(lambda callback: 'ma_' in callback.data)
async def ans_pr(callback: CallbackQuery):
    username = callback.data.lstrip('ma_')
    pk = admin_id(username)
    prod3 = show_my_add_product(pk)
    l = ''
    if show_my_add_product(pk):
        for i in prod3:
            l += ''.join(f'Product name  :{i[2]} \n Product price  :{i[3]} \n Product amount  :{i[4]}')
        await callback.message.answer(f'My add products  :' + '\n' + f"{l}")


@dp.callback_query_handler(lambda callback: '' in callback.data)
async def ans_pr(callback: CallbackQuery):
    username = callback.data.lstrip('ma_')
    pk = admin_id(username)
    prod3 = show_my_add_product(pk)
    l = ''
    if show_my_add_product(pk):
        for i in prod3:
            l += ''.join(f'Product name  :{i[2]} \n Product price  :{i[3]} \n Product amount  :{i[4]}')
        await callback.message.answer(f'My add products  :' + '\n' + f"{l}")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

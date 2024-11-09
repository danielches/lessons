from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from crud_functions import *

api = '8029394283:AAGaz77eRey39M0nKEWcCytMg1I2X8_6TdI'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
products = get_all_products()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Информация"),
            KeyboardButton(text="Рассчитать"),
        ],
        [KeyboardButton(text="Купить")],
        [KeyboardButton(text="Регистрация")]
    ], resize_keyboard=True
)

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ]
)

ikbforproducts = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Product1", callback_data="product_buying"),
         InlineKeyboardButton(text="Product2", callback_data="product_buying")],
        [InlineKeyboardButton(text="Product3", callback_data="product_buying"),
         InlineKeyboardButton(text="Product4", callback_data="product_buying")]
    ]
)


@dp.message_handler(commands=['start'])
async def urban_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ikb)


@dp.message_handler(text=['Информация'])
async def get_info(message):
    await message.answer('Это информация о боте')


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f"Возраст {data['age']}, рост {data['growth']}, вес {data['weight']}")
    res = (10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5)
    await message.answer(f"Ваша норма калорий: {res}")
    await state.finish()

@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    data = await state.get_data()
    if is_included(data["username"]):
        await message.answer("Пользователь существует, введите другое имя(только латинский алфавит):")
        await RegistrationState.username.set()
    else:
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'],data['email'], data['age'])
    await state.finish()

@dp.message_handler(text=["Купить"])
async def get_buying_list(message):
    for number in range(1, 4+1):
        await message.answer(f"Название: {products[number-1][1]} | Описание: {products[number-1][2]} | Цена: {products[number-1][3]}")
        with open(f"pictures/product{number}.png", 'rb') as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=ikbforproducts)


@dp.callback_query_handler(text=["product_buying"])
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

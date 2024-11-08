from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Информация"),
            KeyboardButton(text="Рассчитать"),
            KeyboardButton(text="Купить")
        ]
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


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


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


@dp.message_handler(text=["Купить"])
async def get_buying_list(message):
    for number in range(1, 4 + 1):
        await message.answer(f"Название: Product{number} | Описание: описание {number} | Цена: {number * 100}")
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

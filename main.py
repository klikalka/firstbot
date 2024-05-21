from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import  get_keyboard1, get_keyboard2
from keyboard.key_inline import get_keyboard_inline, get_key_inline2, get_key_inline3, get_key_inline4
from datetime import datetime
import random

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Запуск бота'),
        types.BotCommand(command='/help', description='Помощь от бота'),
        types.BotCommand(command='/cat', description='Коты'),
        types.BotCommand(command='/hau', description='Как дела?'),
        types.BotCommand(command='/hehe', description='Анекдот')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('привет, я неформал', reply_markup= get_key_inline3() )

@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('>>', reply_markup=get_key_inline4())


@dp.callback_query_handler(lambda c: c.data == 'lol')
async def lol(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f'Я не клоун')


@dp.callback_query_handler(lambda c: c.data == 'ioi')
async def ioi(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f'ъуъуъуъ')

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('<<', reply_markup=get_key_inline3())

@dp.callback_query_handler(lambda c: c.data == 'send')
async def send(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f'Что за зоопарк вы тут развели?')

@dp.callback_query_handler(lambda c: c.data == 'send_random')
async def random_number(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f'Случайное число: {random_number}')
random_number = random.randint(1, 100)

@dp.callback_query_handler(lambda c: c.data == 'time')
async def time(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f'Сейчас: {time}')
time = datetime.now().strftime("%H:%M:%S")




@dp.message_handler(lambda message: message.text == 'Отправь злого кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://i.pinimg.com/736x/01/60/09/016009b63930c8862755f9fa6e3bf511.jpg', caption='я хочу домой', reply_markup=get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Отправь шутку')
async def button_2_click(message: types.Message):
    await message.answer('Я не клоун')

@dp.message_handler(lambda message: message.text == 'Ыъыъы')
async def button_3_click(message: types.Message):
    await message.answer('ъуъуъуъ')

@dp.message_handler(lambda message: message.text == '>>')
async def button_4_click(message: types.Message):
    await message.answer('>>', reply_markup=get_keyboard2())

@dp.message_handler(lambda message: message.text == 'Отправь злого пса')
async def button_5_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://i.pinimg.com/736x/03/1c/4b/031c4b2665938050584f83db949e8dc6.jpg')

@dp.message_handler(lambda message: message.text == 'Отправь злого хомяка')
async def button_6_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://i.pinimg.com/736x/47/ce/f2/47cef2d8c4866bb7bc90f0ccd1aa5d13.jpg', caption='Мы вам рекомендуем ознакомиться со статьями ниже', reply_markup=get_key_inline2())

@dp.message_handler(lambda message: message.text == 'Отправь...')
async def button_7_click(message: types.Message):
    await message.reply('Что за зоопарк вы тут развели?')

@dp.message_handler(lambda message: message.text == '<<')
async def button_8_click(message: types.Message):
    await message.answer('<<', reply_markup=get_keyboard1())

@dp.message_handler(commands='help')
async def start(message: types.Message):
    await message.reply('себе помоги')

@dp.message_handler(commands='hehe')
async def start(message: types.Message):
    await message.reply('Что может быть хуже, чем мальчика, которого сбила машина? Холо.......')

@dp.message_handler(commands='hau')
async def start(message: types.Message):
    await message.answer('плохо')

@dp.message_handler(commands='cat')
async def start(message: types.Message):
    await message.answer('- ˕ •マ')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup= on_startup)


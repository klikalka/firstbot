from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

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
    await message.answer('привет, я неформал')


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

@dp.message_handler(commands='hehe')
async def start(message: types.Message):
    await message.reply('Что может быть хуже, чем мальчика, которого сбила машина? Холо.......')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup= on_startup)


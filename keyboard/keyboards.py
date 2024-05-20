from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Отправь злого кота')
    button_2 = KeyboardButton('Отправь шутку')
    button_3 = KeyboardButton('Ыъыъы')
    button_4 = KeyboardButton('>>')
    keyboard.add(button_1,button_2,button_3,button_4)
    return keyboard

def get_keyboard2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_5 = KeyboardButton('Отправь злого пса')
    button_6 = KeyboardButton('Отправь злого хомяка')
    button_7 = KeyboardButton('Отправь...')
    button_8 = KeyboardButton('<<')
    keyboard_2.add(button_5,button_6,button_7,button_8)
    return keyboard_2

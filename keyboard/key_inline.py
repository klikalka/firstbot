from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Ультра mega cool анрил видео с raccoon', url='https://youtu.be/DpjwUfwetx8')
    but_inline2 = InlineKeyboardButton('Быстрый заработок', url='https://youtu.be/k_a_nbpVpUo')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
def get_key_inline2():
    keyboard_inline2 = InlineKeyboardMarkup(row_width=2)
    but_inline3 = InlineKeyboardButton('Факты о которых никто не знал', url='https://news.qq.com/ch/auto/')
    but_inline4 = InlineKeyboardButton('Трешовая история о которой тяжело молчать', url='https://www.techinsider.ru/science/821283-homyaki-pitanie-privychki-i-drugie-interesnye-fakty/#:~:text=%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%BD%D0%BE%20ASPCA%2C%20%D1%85%D0%BE%D0%BC%D1%8F%D0%BA%D0%B8%20%D0%B2%D0%B5%D0%B4%D1%83%D1%82%20%D0%BD%D0%BE%D1%87%D0%BD%D0%BE%D0%B9,%D0%B8%D0%B7%D0%B1%D0%B5%D0%B3%D0%B0%D1%82%D1%8C%20%D1%81%D1%82%D0%BE%D0%BB%D0%BA%D0%BD%D0%BE%D0%B2%D0%B5%D0%BD%D0%B8%D1%8F%20%D1%81%20%D0%B6%D0%B0%D1%80%D0%BA%D0%B8%D0%BC%20%D0%BA%D0%BB%D0%B8%D0%BC%D0%B0%D1%82%D0%BE%D0%BC.')
    keyboard_inline2.add( but_inline3, but_inline4)
    return keyboard_inline2

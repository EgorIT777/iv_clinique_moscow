from loader import bot
from telebot import types

administrations = {
    "Брылевская Инна Валерьевна": "\n-генеральный директор",
    "Брылевский Сергей Александрович": "\n-главный врач",
    "Самойлова Оксана Юрьевна": "-\nоперационный директор",
    "Мурзабаева Наталья Александровна": "\n-администратор"
}

administrations_photo = {
    "Брылевская Инна Валерьевна": "https://i.yapx.ru/VfWkG.png",
    "Брылевский Сергей Александрович": "https://i.yapx.ru/VfWdU.png",
    "Самойлова Оксана Юрьевна": "https://i.yapx.ru/VfXKL.png",
    "Мурзабаева Наталья Александровна": "https://i.yapx.ru/VfXSL.png"
}


def get_main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_administrations = types.InlineKeyboardButton("Администрация", callback_data="admin")
    keyboard.row(button_administrations)
    return keyboard


@bot.message_handler(commands=['Администрация'])
def show_administrations(message):
    for name, description in administrations.items():
        photo_url = administrations_photo.get(name)
        if photo_url:
            bot.send_photo(message.chat.id, photo_url, caption=f"{name}\n{description}")
        else:
            bot.send_message(message.chat.id, f"{name}\n{description}")



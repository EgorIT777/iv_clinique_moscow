from loader import bot
from telebot import types

therapists = {
    "Басова Елена Александровна": "\n-Терапевт",
    "Лосева Марина Андреевна": "\n-Терапевт",
}

therapists_photos = {
    "Басова Елена Александровна": "https://ibb.co/HtRLSqH",
    "Лосева Марина Андреевна": "https://ibb.co/V9Q8ZK2"
}

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_therapists = types.InlineKeyboardButton("Терапевты")
keyboard.add(button_therapists)


@bot.message_handler(commands=["Терапевты"])
def show_therapists(message):
    bot.send_message(message.chat.id, "Наши терапевты:")
    for name, description in therapists.items():
        photo_url = therapists_photos.get(name)
        if photo_url:
            bot.send_photo(message.chat.id, photo_url, caption=f"{name}\n{description}")
        else:
            bot.send_message(message.chat.id, f"{name}\n{description}")



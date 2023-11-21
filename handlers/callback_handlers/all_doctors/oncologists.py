from loader import bot
from telebot import types

oncologists = {
    "Брылевский Сергей Александрович": "\n-Онколог",
    "Симакова Юлия Андреевна": "\n-Онколог"
}

oncologists_photos = {
    "Брылевский Сергей Александрович": "https://i.yapx.ru/VfWdU.png",
    "Симакова Юлия Андреевна": "https://wampi.ru/image/YcYOIv7"
}

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_oncologists = types.KeyboardButton("Онкологи")
keyboard.add(button_oncologists)


@bot.message_handler(commands=["Онкологи"])
def show_oncologists(message):
    bot.send_message(message.chat.id, "Наши онкологи:")
    for name, description in oncologists.items():
        photo_url = oncologists_photos.get(name)
        if photo_url:
            bot.send_photo(message.chat.id, photo_url, caption=f"{name}\n{description}")
        else:
            bot.send_message(message.chat.id, f"{name}\n{description}")
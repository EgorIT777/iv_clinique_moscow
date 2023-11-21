from loader import bot
from telebot import types

neurologists = {
    "Чеканина Нона Александровна": "\n-Невролог",
    "Осипова Алёна Евгеньевна": "\n-Невролог"
}

neurologists_photos = {
    "Чеканина Нона Александровна": "https://i.yapx.ru/VfSAd.png",
    "Осипова Алёна Евгеньевна": "https://i.yapx.ru/VfSBT.png"
}

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_neurologists = types.KeyboardButton("Неврологи")
keyboard.add(button_neurologists)


@bot.message_handler(commands=["Неврологи"])
def show_neurologists(message):
    bot.send_message(message.chat.id, "Наши неврологи: ")
    for name, description in neurologists.items():
        photo_url = neurologists_photos.get(name)
        if photo_url:
            bot.send_photo(message.chat.id, photo_url, caption=f"{name}\n")
        else:
            bot.send_message(message.chat.id, f"{name}\n")
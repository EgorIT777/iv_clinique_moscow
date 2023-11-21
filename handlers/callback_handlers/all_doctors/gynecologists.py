from loader import bot

from telebot import types

gynecologists = {
    "Симакова Юлия Андреевна": "\n-Гинеколог",
    "Сергеева Анастасия Юрьевна": "\n-Гинеколог"
}

gynecologists_photos = {
    "Симакова Юлия Андреевна": "https://i.yapx.ru/VfR7z.png",
    "Сергеева Анастасия Юрьевна": "https://i.yapx.ru/VfR80.png"
}

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_gynecologists = types.KeyboardButton("Гинекологи")
keyboard.add(button_gynecologists)


@bot.message_handler(commands=["Гинекологи"])
def show_gynecologists(message):
    for name, description in gynecologists.items():
        photo_url = gynecologists_photos.get(name)
        if photo_url:
            bot.send_photo(message.chat.id, photo_url, caption=f"{name}\n{description}")
        else:
            bot.send_message(message.chat.id, f"{name}\n{description}")
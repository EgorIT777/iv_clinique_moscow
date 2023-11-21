from loader import bot
from telebot import types

cosmetologists = {
    "Брылевская Инна Валерьевна": "\n-Косметолог",
    "Доброгорская Елена Сергеевна": "\n-Косметолог",
    "Лосева Марина Дмитриевна": "\n-Косметолог",
    "Холод Ольга Владимировна": "\n-Косметолог"
}

cosmetologists_photos = {
    "Брылевская Инна Валерьевна": "https://i.yapx.ru/VfWkG.png",
    "Доброгорская Елена Сергеевна": "https://i.yapx.ru/VfWnF.png",
    "Лосева Марина Дмитриевна": "https://i.yapx.ru/VfWoP.png",
    "Холод Ольга Владимировна": "https://wampi.ru/image/YcYez0n"
}

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_cosmetologists = types.InlineKeyboardButton("Косметология")
keyboard.add(button_cosmetologists)


@bot.message_handler(commands=["Косметологи"])
def show_cosmetologists(message):
    bot.send_message(message.chat.id, "Наши косметологи:")
    for name, description in cosmetologists.items():
        photo_url = cosmetologists_photos.get(name)
        if photo_url:
            bot.send_photo(message.chat.id, photo_url, caption=f"{name}\n{description}")
        else:
            bot.send_message(message.chat.id, f"{name}\n{description}")

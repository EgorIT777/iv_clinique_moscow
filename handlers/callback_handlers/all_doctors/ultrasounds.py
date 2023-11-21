from loader import bot
from telebot import types

ultrasound_doctors = {
    "Басова Елена Александровна": "\n-Врач УЗИ",
    "Брылевский Сергей Александрович": "\n-Врачи УЗИ",
    "Симакова Юлия Андреевна": "\n-Врач УЗИ",
    "Сергеева Анастасия Юрьевна": "\n-Врач УЗИ",
    "Храмченко Наталья Васильевна": "\n-Врач УЗИ"
}


ultrasound_doctors_photo = {
    "Басова Елена Александровна": "https://i.yapx.ru/VfR36.png",
    "Брылевский Сергей Александрович": "https://i.yapx.ru/VfWdU.png",
    "Симакова Юлия Андреевна": "https://i.yapx.ru/VfR7z.png",
    "Сергеева Анастасия Юрьевна": "https://i.yapx.ru/VfR80.png",
    "Храмченко Наталья Васильевна": "https://ibb.co/bNqYC18"
}


keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_ultrasounds = types.KeyboardButton("Узи")
keyboard.add(button_ultrasounds)


@bot.message_handler(commands=["УЗИ"])
def show_ultrasound_doctors(message):
    bot.send_message(message.chat.id, "Врачи УЗИ:")
    for name, description in ultrasound_doctors.items():
        photo_url = ultrasound_doctors_photo.get(name)
        if photo_url:
            bot.send_photo(message.chat.id, photo_url, caption=f"{name}\n{description}")
        else:
            bot.send_message(message.chat.id, f"{name}\n")

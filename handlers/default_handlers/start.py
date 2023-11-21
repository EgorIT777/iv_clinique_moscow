from loader import bot

from telebot import types


@bot.message_handler(commands=["start"])
def start_command(message):
    image_url = "https://ibb.co/2nF3jfX"
    bot.send_photo(chat_id=message.chat.id, photo=image_url)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)

    commands = [
        "/Приём", "/Услуги", "/Консультация", "/Локация",
        "/Терапевты", "/Гинекологи", "/Неврологи",
        "/Онкологи", "/Косметологи", "/УЗИ",
        "/Администрация", "/Телеграм", "/YouTube",
        "/Вк", "/Instagram", "/Ok", "/Описание"
    ]

    for command in commands:
        markup.add(types.KeyboardButton(command))

    bot.send_message(
        chat_id=message.chat.id,
        text="Добро пожаловать в клинику интегративной медицины IV clinique. ❤️\n\n"
             "Дарим 1000₽ каждому новому пациенту!\n\n"
             "Пожалуйста, выберите комнаду:",
        reply_markup=markup
    )

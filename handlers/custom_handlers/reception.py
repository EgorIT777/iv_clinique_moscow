from loader import bot
from telebot import types


@bot.message_handler(commands=["Приём"])
def start_command(message):
    url = "https://i.yapx.ru/Veudc.png"
    bot.send_photo(chat_id=message.chat.id, photo=url)
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Наш сайт", url="https://www.ivclinique.ru")
    markup.add(button1)
    bot.send_message(message.chat.id, "Чтобы записатьс на приём, перейдите на сайт клиники или"
                                      "позвоните по телефону: +7(989) 580-42-62", reply_markup=markup)

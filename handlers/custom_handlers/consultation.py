from loader import bot
from telebot import types


@bot.message_handler(commands=["Консультация"])
def show_online_consultation(message):
    url = "https://ibb.co/4tCgJ2Q"
    bot.send_photo(chat_id=message.chat.id, photo=url)
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Записаться",
                                         url="https://optimusmgn.tilda.ws/")
    markup.add(button1)
    bot.send_message(message.chat.id, "Приглашаем вас на онлайн консультацию", reply_markup=markup)
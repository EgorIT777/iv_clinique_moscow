from loader import bot
from telebot import types


@bot.message_handler(commands=["Услуги"])
def services_handler(message):
    url = "https://i.yapx.cc/Veefu.jpg"
    bot.send_photo(chat_id=message.chat.id, photo=url)
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Задать вопрос", url="https://ivclinique.ru/contacts")
    markup.add(button1)
    bot.send_message(message.chat.id, text= "Наша клиника предлагает широкий спектр услуг интегративной медицины,"
                                            "включая онкологию, маммологию, гинекологию, косметологию,"
                                            "УЗИ, неврологию, IV-терапию, карбокситерапию.\n"
                                            "Дайте мне знать, если у вас есть какие-либо "
                                            "конкретные вопросы.", reply_markup=markup)
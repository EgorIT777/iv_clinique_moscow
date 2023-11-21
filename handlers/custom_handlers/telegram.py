from loader import bot
from telebot import types


@bot.message_handler(commands=["Телеграм"])
def telegram_channel(message):
    telegram_url = f"https://t.me/ivcliniqueMoscow"
    button = types.InlineKeyboardButton(text="Подписаться", url=telegram_url)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button)
    bot.send_message(chat_id=message.chat.id, text="Подпишись на наш телеграм канал", reply_markup=keyboard)
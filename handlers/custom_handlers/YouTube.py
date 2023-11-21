from loader import bot
from telebot import types


@bot.message_handler(commands=["YouTube"])
def youtube_sub(message):
    youtube_url = f"https://www.youtube.com/@ivcliniquemoscow3647"
    button = types.InlineKeyboardButton(text="Подписаться", url=youtube_url)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button)
    bot.send_message(chat_id=message.chat.id, text="Подпишись на наш YouTube канал", reply_markup=keyboard)
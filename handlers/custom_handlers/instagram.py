from loader import bot
from telebot import types

instagram_username = "iv.clinique.moscow"


@bot.message_handler(commands=["Instagram"])
def insta_sub(message):
    instagram_url = f"https://www.instagram.com/{instagram_username}"
    button = types.InlineKeyboardButton(text="Подписаться", url=instagram_url)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button)
    bot.send_message(chat_id=message.chat.id, text="Наш аккаунт в instagram", reply_markup=keyboard)

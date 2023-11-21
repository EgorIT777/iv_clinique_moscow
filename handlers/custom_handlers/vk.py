from loader import bot
from telebot import types


@bot.message_handler(commands=["Вк"])
def vk_sub(message):
    vk_url = f"https://vk.com/iv_clinique"
    button = types.InlineKeyboardButton(text="Подписаться", url=vk_url)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button)
    bot.send_message(chat_id=message.chat.id, text="Наша группа в ВКонтакте", reply_markup=keyboard)
from loader import bot
from telebot import types


@bot.message_handler(commands=["Ok"])
def ok_sub(message):
    ok_url = f"https://ok.ru/group/70000000285704"
    button = types.InlineKeyboardButton(text="Подписаться", url=ok_url)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button)
    bot.send_message(chat_id=message.chat.id, text="Группа в Одноклассниках", reply_markup=keyboard)

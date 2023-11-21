from loader import bot


@bot.message_handler(commands=["Локация"])
def send_locations(message):
    latitude = 55.73327
    longitude = 37.41861
    bot.send_message(chat_id=message.chat.id, text="Будем рады вас видеть!")
    bot.send_location(message.chat.id, latitude, longitude)

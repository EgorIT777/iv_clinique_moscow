from loader import bot


@bot.message_handler(commands=["Описание"])
def about_us(message):
    image_url = "https://ibb.co/DDGCXwS"
    bot.send_photo(chat_id=message.chat.id, photo=image_url)
    clinique_description = "Клиника интегративной медицины и косметологии 'IV Clinique' - это современная клиника,\n"\
                           "которая использует системный подход в лечении различных заболеваний.\n"\
                           "Мы не лечим симптомы. Мы ищем причину заболевания, работаем с ней, в результате чего "\
                           "проходят все тревожащие вас симптомы." \
                           " 'Сердце' нашей клиники - это наши доктора. Все специалисты высоко квалифицированные "\
                           "профессионалы медицины - терапевт, невролог, гинеколог, онколог, маммолог, психолог, "\
                           "специалист " \
                           "УЗИ.\n" \
                           "Все доктора клиники проходят постоянное обучение в области превентивной и интегративной " \
                           "медицины, большинство наших врачей выпускников Международного института 'Prevent Age'."
    bot.send_message(chat_id=message.chat.id, text=clinique_description)

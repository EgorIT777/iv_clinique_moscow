from loader import bot
import handlers  # noqa
from telebot.custom_filters import StateFilter


if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    bot.polling(none_stop=True)

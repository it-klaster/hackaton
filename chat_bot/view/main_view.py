import random
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from chat_bot.constants import Buttons


class MainView:
    greeting_message = "Выберите действие:"
    unknown_msg = ['Не понял, повторите', 'Я не знаю такой команды.', 'Это ни на что не похоже...']

    def __init__(self, bot):
        self.bot = bot

    def main_menu(self, chat_id):
        keyboard = [
            [KeyboardButton(text=Buttons.help)],
            [KeyboardButton(text=Buttons.get_events)],
            [KeyboardButton(text=Buttons.register)]
        ]
        markup = ReplyKeyboardMarkup(keyboard=keyboard)
        return self.bot.send_message(chat_id=chat_id,
                                     text=self.greeting_message,
                                     reply_markup=markup)

    def unknown(self, chat_id):
        msg = random.choice(self.unknown_msg)
        return self.bot.send_message(chat_id=chat_id, text=msg)


    def help(self, chat_id):
        msg = """Я могу:\n/help - Эта подсказка\n/events - Рассказать, какие события/работы/мероприятия запланировнны по адресу.\n/register - Подписаться на объявления по определенному адресу"""
        return self.bot.send_message(chat_id=chat_id, text=msg)
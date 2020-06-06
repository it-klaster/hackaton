from telegram import ReplyKeyboardRemove
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from chat_bot.constants import Buttons
from chat_bot.view.registration_view import RegistrationView

ask_adr_msg = "Здравствуйте, {}! \nУкажите адрес, чтобы получить информацию об актуальных событиях"

class GetEventView(RegistrationView):

    def ask_adress(self, chat_id, user):
        answer = ask_adr_msg.format(user.first_name)
        keyboard = [
            [KeyboardButton(text=Buttons.cancel)]
        ]
        markup = ReplyKeyboardMarkup(keyboard=keyboard)
        return self.bot.send_message(chat_id=chat_id, text=answer, reply_markup=markup)

    def reply_success(self, chat_id, data):
        events = data['events']
        adr = data['adr']
        event_names = [event.name for event in events]
        list = '\n-'.join(event_names)
        answer = f'Список событий по адресу: {adr.name}:\n {list}'


        if not list:
            return self.bot.send_message(chat_id=chat_id,
                                 text=f'Событий по адресу {adr.name} не найдено.')


        return self.bot.send_message(chat_id=chat_id,
                                 text=answer)


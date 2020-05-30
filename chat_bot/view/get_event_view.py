from telegram import ReplyKeyboardRemove

from chat_bot.view.registration_view import RegistrationView

ask_adr_msg = "Здравствуйте, {}! \nУкажите адрес, чтобы получить информацию об актуальных событиях"

class GetEventView(RegistrationView):

    def ask_adress(self, chat_id, user):
        answer = ask_adr_msg.format(user.first_name)
        return self.bot.send_message(chat_id=chat_id, text=answer)

    def reply_success(self, chat_id, adr, events):
        # delete menu
        event_names = [event.name for event in events]
        list = '\n-'.join(event_names)
        answer = f'Список событий по адресу: {adr.name}:\n {list}'
        reply_markup = ReplyKeyboardRemove()
        if not list:
            return self.bot.send_message(chat_id=chat_id,
                                 text=f'Событий по адресу {adr.name} не найдено.',
                                 reply_markup=reply_markup)


        return self.bot.send_message(chat_id=chat_id,
                                 text=answer,
                                 reply_markup=reply_markup)


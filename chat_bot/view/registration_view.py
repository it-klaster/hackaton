

class RegistrationView:

    def __init__(self, bot):
        self.bot = bot


    def ask_adress(self, chat_id, user):
        answer = f"Здравствуйте, {user.first_name}! \nЧтобы получать уведомления сервиса 'Умный город',  укажите адрес дома"
        return self.bot.send_message(chat_id=chat_id, text=answer)


class MainView:
    greeting_message = "Здесь будет основное меню"

    def __init__(self, bot):
        self.bot = bot
        # self.message_sender = MessageSender(bot=bot)
        # self.logger = Logger.get_logger()

    def send_greeting_message(self, chat_id):
        # keyboard = [[
        #     KeyboardButton(text=Buttons.back_to_main_menu),
        #     KeyboardButton(text=Buttons.sample_button),
        # ]]
        # markup = ReplyKeyboardMarkup(keyboard=keyboard)
        self.bot.send_message(chat_id=chat_id, text=self.greeting_message)
        # self.logger.info(inspect.stack()[0][3])

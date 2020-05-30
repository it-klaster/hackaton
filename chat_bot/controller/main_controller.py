from telegram.ext import ConversationHandler, CommandHandler, RegexHandler, MessageHandler

from chat_bot.view.main_view import MainView


class MainController:

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.main_view = MainView(bot=dispatcher.bot)
        self.default_handlers = [
            CommandHandler(command="start", callback=self.main_menu)
        ]
        self.__process_handlers()

    def main_menu(self, update, context):
        chat_id = update.message.chat_id
        self.main_view.send_greeting_message(chat_id)

    def process_options(self, update, context):
        pass

    def __process_handlers(self):
        # self.dispatcher.add_handler(CommandHandler(command="start", callback=self.main_menu))
        # self.dispatcher.add_handler(CommandHandler(command="register", callback=self.main_menu))
        pass


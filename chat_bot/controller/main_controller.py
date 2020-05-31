from telegram.ext import ConversationHandler, CommandHandler, RegexHandler, MessageHandler, Filters

from chat_bot.constants import Buttons
from chat_bot.utils import get_logging, send_typing_action
from chat_bot.view.main_view import MainView
logger = get_logging()


class MainController:
    name = 'main'

    def __init__(self, dispatcher, controllers=None):
        self.dispatcher = dispatcher
        self.view = MainView(bot=dispatcher.bot)
        # init child controllers
        if controllers:
            for controller in controllers:
                setattr(self, controller.name, controller)

        self.default_handlers = [
            CommandHandler(command="start", callback=self.main_menu),

            CommandHandler(command="help", callback=self.help),
            MessageHandler(Filters.text(Buttons.help), self.help),
            MessageHandler(Filters.text(Buttons.cancel), self.main_menu)
        ]

        self.__process_handlers()

    @send_typing_action
    def help(self,  update, context):
        return self.view.help(update.message.chat_id)

    @send_typing_action
    def main_menu(self, update, context):
        chat_id = update.message.chat_id
        return self.view.main_menu(chat_id)

    def unknown(self, update, context):
        self.view.unknown(update.message.chat_id)


    def __process_handlers(self):
        pass



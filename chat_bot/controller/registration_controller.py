from telegram.ext import ConversationHandler, StringCommandHandler, MessageHandler, Filters, RegexHandler

from chat_bot.controller.main_controller import MainController
from chat_bot.utils import get_logging
from chat_bot.view.registration_view import RegistrationView

logger = get_logging()

class RegistrationController(MainController):

    states_dict = {
        "START_REGISTRATION": 0,
        "FIRST_ASK_ADRESS": 1,
        "SPECIFY_ADRESS": 2,
        "ASK_AGAIN": 3,
        "SUCCESS": 4
    }

    def __init__(self, dispatcher):
        super().__init__(dispatcher)
        self.dispatcher = dispatcher
        self.__process_handlers()
        self.view = RegistrationView(dispatcher.bot)

    def init_state(self, update, context):
        chat_id = update.message.chat_id
        user = update.message.from_user
        self.view.ask_adress(chat_id, user)
        return self.states_dict['START_REGISTRATION']

    def ask_adress(self, update, context):
        return


    def __process_handlers(self):
        conversation_handler = ConversationHandler(entry_points=[MessageHandler(Filters.text('/register'), self.init_state)],
                                                   states={
                                                       self.states_dict["START_REGISTRATION"]: self.default_handlers + [MessageHandler(Filters.text, self.ask_adress)]
                                                   }, fallbacks=[], allow_reentry=True)
        self.dispatcher.add_handler(conversation_handler)

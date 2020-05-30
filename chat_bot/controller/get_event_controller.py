from telegram.ext import ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

from chat_bot.controller.registration_controller import RegistrationController
from chat_bot.services import search_address, get_events
from chat_bot.utils import send_typing_action, get_logging
from chat_bot.view.get_event_view import GetEventView

logger = get_logging()

class GetEventController(RegistrationController):

    states_dict = {
        "WAIT_INPUT": 1,
        "CHOOSE_OPTIONS": 2,
        "REPEAT": 3,
        "SUCCESS": 4
    }

    def __init__(self, dispatcher):
        super().__init__(dispatcher)
        self.dispatcher = dispatcher
        self.__process_handlers()
        self.view = GetEventView(dispatcher.bot)
        self.address_options = []


    @send_typing_action
    def whait_input(self, update, context):
        chat_id = update.message.chat_id
        user = update.message.from_user
        self.view.ask_adress(chat_id, user)
        return self.states_dict['WAIT_INPUT']

    @send_typing_action
    def process_options(self, update, context):
        chat_id = update.effective_chat.id
        adress_name = update.callback_query.data
        if adress_name not in self.address_options:
            return self.specify_adress(update, context)

        adr = search_address(adress_name)
        if not adr:
            self.view.not_found(chat_id, adress_name)
            return self.states_dict["REPEAT"]

        events = get_events(adr[0].id)
        self.view.reply_success(chat_id, adr, events)

        return self.states_dict["WAIT_INPUT"]



    def __process_handlers(self):
        conversation_handler = ConversationHandler(entry_points=[MessageHandler(Filters.text('/events'), self.whait_input)],
                                                   states={
                                                       self.states_dict["WAIT_INPUT"]: self.default_handlers + [MessageHandler(Filters.text, self.specify_adress)],
                                                       self.states_dict["REPEAT"]: self.default_handlers + [MessageHandler(Filters.text, self.repeat)],
                                                       self.states_dict["CHOOSE_OPTIONS"]: self.default_handlers + [CallbackQueryHandler(self.process_options)],
                                                       # self.states_dict["SUCCESS"]: self.default_handlers + [MessageHandler(Filters.text, self.change_adress)]
                                                   }, fallbacks=[
                                                        self.default_handlers
                                                    ], allow_reentry=True)
        self.dispatcher.add_handler(conversation_handler)
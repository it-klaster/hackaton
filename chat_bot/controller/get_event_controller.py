from telegram.ext import ConversationHandler, MessageHandler, Filters, CallbackQueryHandler, CommandHandler

from chat_bot.constants import Buttons
from chat_bot.controller.main_controller import MainController
from chat_bot.controller.registration_controller import RegistrationController
from chat_bot.services import search_address, get_events
from chat_bot.utils import send_typing_action, get_logging, normalize_adrs
from chat_bot.view.get_event_view import GetEventView

logger = get_logging()

class GetEventController(MainController):

    name = 'event'

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
    def repeat(self, update, context):
        self.specify_adress(update, context)

    @send_typing_action
    def specify_adress(self, update, context):
        if hasattr(update, 'callback_query'):
            chat_id = update.message.chat_id
            msg = update.message.text
        else:
            chat_id = update.callback_query.chat_instance
            msg = update.message.text
        normal_msg = normalize_adrs(msg)
        addresses = search_address(normal_msg)

        if not addresses:
            self.view.not_found(chat_id, msg)
            return self.states_dict['REPEAT']

        # TODO: Addd interaction for alone get address
        # if len(addresses) == 1:
        #     return self.process_options(addresses[0])

        if len(addresses) > 20:
            self.view.too_many_found(chat_id, msg, len(addresses))
            return self.states_dict['REPEAT']

        if len(addresses) <= 20:
            self.view.choose_address(chat_id, addresses)
            self.address_options = [adr.name for adr in addresses]
            return self.states_dict['CHOOSE_OPTIONS']

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

        self.view.reply_success(chat_id, {'adr': adr[0], 'events': events})

        return self.states_dict["WAIT_INPUT"]

    def cancel(self, update, context):
        return ConversationHandler.END


    def __process_handlers(self):
        self.conversation_handler = ConversationHandler(entry_points=[MessageHandler(Filters.text('/events'), self.whait_input),
                                                                      MessageHandler(Filters.text(Buttons.get_events), self.whait_input)],
                                                       states={
                                                           self.states_dict["WAIT_INPUT"]: self.default_handlers + [
                                                               MessageHandler(Filters.text, self.specify_adress)
                                                           ],
                                                           self.states_dict["REPEAT"]: self.default_handlers + [
                                                               MessageHandler(Filters.text, self.repeat)],
                                                           self.states_dict["CHOOSE_OPTIONS"]: self.default_handlers + [
                                                               CallbackQueryHandler(self.process_options)
                                                           ],
                                                           # self.states_dict["SUCCESS"]: self.default_handlers + [MessageHandler(Filters.text, self.change_adress)]
                                                       }, fallbacks=[
                                                            # MessageHandler(Filters.text, self.cancel)
                                                        ], allow_reentry=True,

                                                        )
        self.dispatcher.add_handler(self.conversation_handler)

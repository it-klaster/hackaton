from telegram.ext import ConversationHandler, MessageHandler, Filters, CallbackQueryHandler, CommandHandler

from chat_bot.constants import Buttons
from chat_bot.controller.main_controller import MainController
from chat_bot.services import search_address, get_events
from chat_bot.utils import send_typing_action, get_logging, normalize_adrs, find_address, normalize_from_geocoder
from chat_bot.view.get_event_view import GetEventView

logger = get_logging()

class GetEventController(MainController):

    name = 'event'

    states_dict = {
        "WAIT_INPUT": 1,
        "CHOOSE_OPTIONS": 2,
        "SUCCESS": 3
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
    def specify_adress(self, update, context):
        chat_id = update.message.chat_id
        msg = update.message.text
        if msg:
            normal_msg = normalize_adrs(msg)
            addresses = search_address(normal_msg)

        # try to find by geolocation
        loc = update.message.location
        if loc:
            # We catch Filter.location
            msg = find_address(longitude=loc.longitude, latitude=loc.latitude)
            if not normalize_from_geocoder(msg):
                self.view.not_found(chat_id, 'ваши координаты')
                return self.states_dict['WAIT_INPUT']
            normal_msg = normalize_from_geocoder(msg)
            addresses = search_address(normal_msg)

        if not addresses:
            self.view.not_found(chat_id, msg)
            return self.states_dict['WAIT_INPUT']

        # TODO: Add interaction for alone get address
        # if len(addresses) == 1:
        #     return self.process_options(addresses[0])

        if len(addresses) > 20:
            self.view.too_many_found(chat_id, msg, len(addresses))
            return self.states_dict['WAIT_INPUT']

        if len(addresses) <= 20:
            self.view.choose_address(chat_id, addresses)
            self.address_options = [adr.name for adr in addresses]
            return self.states_dict['CHOOSE_OPTIONS']



    @send_typing_action
    def process_options(self, update, context):

        chat_id = update.effective_chat.id
        adress_name = update.callback_query.data
        if adress_name not in self.address_options:
            return self.specify_adress(update, context)

        adr = search_address(adress_name)
        if not adr:
            self.view.not_found(chat_id, adress_name)
            return self.states_dict["WAIT_INPUT"]

        events = get_events(adr[0].id)

        self.view.reply_success(chat_id, {'adr': adr[0], 'events': events})

        return self.states_dict["WAIT_INPUT"]


    def __process_handlers(self):
        self.conversation_handler = ConversationHandler(entry_points=[MessageHandler(Filters.text('/events'), self.whait_input),
                                                                      MessageHandler(Filters.text(Buttons.get_events), self.whait_input)],
                                                        states={
                                                           self.states_dict["WAIT_INPUT"]: [
                                                               MessageHandler(Filters.regex(Buttons.cancel),
                                                                              callback=self.main_menu),
                                                               MessageHandler(Filters.text | Filters.reply, self.specify_adress),
                                                               CallbackQueryHandler(self.process_options)
                                                           ],
                                                           self.states_dict["CHOOSE_OPTIONS"]: [
                                                               MessageHandler(Filters.regex(Buttons.cancel),
                                                                              callback=self.main_menu),

                                                               CallbackQueryHandler(self.process_options)
                                                           ],
                                                        }, fallbacks=[
                                                            # *self.default_handlers
                                                        ], allow_reentry=True,
                                                        )
        self.dispatcher.add_handler(self.conversation_handler)

from telegram.ext import ConversationHandler, MessageHandler, Filters, CallbackQueryHandler, CommandHandler

from chat_bot.constants import Buttons
from chat_bot.controller.main_controller import MainController
from chat_bot.services import search_address, register_user, get_user
from chat_bot.utils import get_logging, normalize_adrs, send_typing_action
from chat_bot.view.registration_view import RegistrationView

logger = get_logging()


class RegistrationController(MainController):

    name = 'registration'

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
        self.view = RegistrationView(dispatcher.bot)
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
        normal_msg = normalize_adrs(msg)
        addresses = search_address(normal_msg)

        if not addresses:
            self.view.not_found(chat_id, msg)
            return self.states_dict['WAIT_INPUT']

        # TODO: Addd interaction for alone get address
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
        adr = update.callback_query.data
        if adr not in self.address_options:
            return self.specify_adress(update, context)

        _from = update.callback_query.from_user
        adr = update.callback_query.data
        user = {'first_name': _from.first_name,
                'last_name': _from.last_name,
                'username': _from.username,
                'telegramm_id': _from.id,
                'address': adr
                }

        registered = register_user(user)
        self.view.reply_success(chat_id, registered)
        # return self.states_dict['WAIT_INPUT']
        return ConversationHandler.BEGIN

    @send_typing_action
    def change_adress(self, update, context):
        chat_id = update.message.chat_id
        _id = update.message.from_user.id
        user = get_user(_id)
        if not user:
            self.view.not_found_user(chat_id)
        return self.view.change_adress(chat_id, user)


    def __process_handlers(self):
        self.conversation_handler = ConversationHandler(entry_points=[MessageHandler(Filters.text('/register'), self.whait_input),
                                                                      MessageHandler(Filters.text(Buttons.register), self.whait_input)],
                                                   states={
                                                       self.states_dict["WAIT_INPUT"]: [MessageHandler(Filters.regex(Buttons.cancel),
                                                                              callback=self.main_menu),
                                                                               MessageHandler(Filters.text, self.specify_adress),
                                                                               CallbackQueryHandler(self.process_options)],
                                                       self.states_dict["CHOOSE_OPTIONS"]: [

                                                                                MessageHandler(Filters.regex(Buttons.cancel), callback=self.main_menu),
                                                                                CallbackQueryHandler(self.process_options)],

                                                       # self.states_dict["SUCCESS"]: self.default_handlers + [MessageHandler(Filters.text, self.change_adress)]
                                                   },
                                                    fallbacks=[
                                                        # MessageHandler(Filters.text('/register'), self.whait_input
                                                        # *self.default_handlers
                                                    ],
                                                        allow_reentry=True)
        self.dispatcher.add_handler(self.conversation_handler)

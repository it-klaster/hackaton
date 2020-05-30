from telegram.ext import ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

from chat_bot.controller.main_controller import MainController
from chat_bot.services import search_address, register_user, get_user
from chat_bot.utils import get_logging, normalize_adrs, send_typing_action
from chat_bot.view.registration_view import RegistrationView

logger = get_logging()

class RegistrationController(MainController):

    states_dict = {
        "FIRST_ASK_ADRESS": 1,
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
    def ask_adress(self, update, context):
        chat_id = update.message.chat_id
        user = update.message.from_user
        self.view.ask_adress(chat_id, user)
        return self.states_dict['FIRST_ASK_ADRESS']

    @send_typing_action
    def repeat(self, update, context):
        self.specify_adress(update, context)

    @send_typing_action
    def specify_adress(self, update, context):
        if not hasattr(update, 'callback_query'):
            chat_id = update.callback_query.chat_instance
            msg = update.message.text
        else:
            chat_id = update.message.chat_id
            msg = update.message.text
        normal_msg = normalize_adrs(msg)
        addresses = search_address(normal_msg)

        if not addresses:
            self.view.not_found(chat_id, msg)
            return self.states_dict['REPEAT']

        if len(addresses) == 1:
            return self.register(addresses[0])

        if len(addresses) > 20:
            self.view.too_many_found(chat_id, msg, len(addresses))
            return self.states_dict['REPEAT']

        if len(addresses) <= 20:
            self.view.choose_address(chat_id, addresses)
            self.address_options = [adr['address'] for adr in addresses]
            return self.states_dict['CHOOSE_OPTIONS']

    @send_typing_action
    def register(self, update, context):
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

        # TODO: Remove when realize adress change
        return ConversationHandler.END

    @send_typing_action
    def change_adress(self, update, context):
        chat_id = update.message.chat_id
        _id = update.message.from_user.id
        user = get_user(_id)
        if not user:
            self.view.not_found_user(chat_id)
        return self.view.change_adress(chat_id, user)


    def __process_handlers(self):
        conversation_handler = ConversationHandler(entry_points=[MessageHandler(Filters.text('/register'), self.ask_adress)],
                                                   states={
                                                       self.states_dict["FIRST_ASK_ADRESS"]: self.default_handlers + [MessageHandler(Filters.text, self.specify_adress)],
                                                       self.states_dict["REPEAT"]: self.default_handlers + [MessageHandler(Filters.text, self.repeat)],
                                                       self.states_dict["CHOOSE_OPTIONS"]: self.default_handlers + [CallbackQueryHandler(self.register)],
                                                       self.states_dict["SUCCESS"]: self.default_handlers + [MessageHandler(Filters.text, self.change_adress)]
                                                   }, fallbacks=[], allow_reentry=True)
        self.dispatcher.add_handler(conversation_handler)

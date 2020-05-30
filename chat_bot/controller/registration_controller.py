from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters

from chat_bot.controller.main_controller import MainController
from chat_bot.view.registration_view import RegistrationView


class RegistrationController(MainController):

    states_dict = {
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

    def ask_adress(self, update, context):
        chat_id = update.message.chat_id
        user = update.message.from_user
        self.view.ask_adress(chat_id, user)


    def __process_handlers(self):
        conversation_handler = ConversationHandler(entry_points=[CommandHandler("FIRST_ASK_ADRESS", self.ask_adress)],
                                                   states={
                                                       # self.states_dict["step_1"]: [
                                                       #                                                        #     MessageHandler(Filters.text, self.final_step)],
                                                       #                                                        # self.states_dict["step_2"]: [
                                                       #                                                        #     MessageHandler(Filters.photo, self.final_step)]
                                                   }, fallbacks=[], allow_reentry=True)
        self.dispatcher.add_handler(conversation_handler)

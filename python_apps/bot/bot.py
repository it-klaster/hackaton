
from telegram.ext import Updater
from settings import Config
from telegram.ext import MessageHandler, Filters

from aoiklivereload import LiveReloader

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

REQUEST_KWARGS = {
    'proxy_url': Config.PROXY
}


class DialogBot:
    def __init__(self, token):
        self.updater = Updater(token, request_kwargs=REQUEST_KWARGS, use_context=True)
        handler = MessageHandler(Filters.text | Filters.command, self.handle_message)
        self.updater.dispatcher.add_handler(handler)
        self.states = ['ASKING_ADRESS', 'GET_ADRESS']
        self.chat_state = {}

    def start(self):
        self.updater.start_polling()

    def handle_message(self, update, context):
        chat_id = update.message.chat_id
        if chat_id not in self.chat_state:
            self.chat_state[chat_id] = 'ASKING_ADRESS'
            answer = "Пожалуйста введите адрес в формате |название улицы|пробел|номер дома|"
            context.bot.send_message(chat_id=update.effective_chat.id, text=answer)


if __name__ == '__main__':
    reloader = LiveReloader()
    reloader.start_watcher_thread()

    dialog_bot = DialogBot(Config.BOT_TOKEN)
    dialog_bot.start()




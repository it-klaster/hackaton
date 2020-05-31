from aoiklivereload import LiveReloader
from telegram.ext import Updater

from chat_bot.controller.get_event_controller import GetEventController
from chat_bot.controller.main_controller import MainController
from chat_bot.controller.registration_controller import RegistrationController
from chat_bot.settings import Config, DEBUG
from chat_bot.utils import get_logging

REQUEST_KWARGS = {}

if DEBUG:
    REQUEST_KWARGS['proxy_url'] = Config.PROXY

class App:
    def __init__(self, token):
        self.log = get_logging()
        self.updater = Updater(token, request_kwargs=REQUEST_KWARGS, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.add_controllers()

    def add_controllers(self):
        main_controller = MainController(dispatcher=self.dispatcher,
                                         controllers=[
                                             RegistrationController(dispatcher=self.dispatcher),
                                             GetEventController(dispatcher=self.dispatcher)
                                         ])
        for handler in main_controller.default_handlers:
            self.dispatcher.add_handler(handler)


    def start(self):
        self.updater.start_polling()


if __name__ == '__main__':

    if DEBUG:
        reloader = LiveReloader()
        reloader.start_watcher_thread()

    app = App(Config.BOT_TOKEN)
    app.start()


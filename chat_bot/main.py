from aoiklivereload import LiveReloader
from telegram.ext import Updater

from chat_bot.controller.get_event_controller import GetEventController
from chat_bot.controller.main_controller import MainController
from chat_bot.controller.registration_controller import RegistrationController
from chat_bot.controller.send_event_controller import SendEventController
from chat_bot.models import Base, engine
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
        self.add_sending_events()

    def add_controllers(self):
        main_controller = MainController(dispatcher=self.dispatcher)
        for handler in main_controller.default_handlers:
            self.dispatcher.add_handler(handler)

        registration_controller = RegistrationController(dispatcher=self.dispatcher)
        get_event_controller = GetEventController(dispatcher=self.dispatcher)

    def add_sending_events(self):
        queue = self.updater.job_queue
        controller = SendEventController(dispatcher=self.dispatcher)
        job_minute = queue.run_repeating(controller.process, interval=60, first=0)

    def start(self):
        self.updater.start_polling()


if __name__ == '__main__':

    if DEBUG:
        reloader = LiveReloader()
        reloader.start_watcher_thread()

    Base.metadata.create_all(bind=engine)

    app = App(Config.BOT_TOKEN)
    app.start()


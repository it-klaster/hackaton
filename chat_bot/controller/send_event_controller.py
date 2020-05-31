from datetime import datetime

from telegram.ext import CallbackContext

from chat_bot.models import session, EventTimer, Event
from chat_bot.settings import DEBUG, Config
from chat_bot.utils import get_logging
from chat_bot.view.send_event_view import SendEventView


logger = get_logging()


class SendEventController:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.view = SendEventView(bot=dispatcher.bot)

    def process(self, context: CallbackContext):
        event_timers = self.get_actual_timers()
        events = []
        for event_timer in event_timers:
            events.extend(event_timer.events)

        events = [e for e in events if e.send_at is None]
        print(events)

        for event in events:
            self.send_event(event)
            event.send_at = datetime.now()
        session.commit()

    def send_event(self, event: Event):
        if DEBUG and Config.DEBUG_USER_ID:
            chat_id = Config.DEBUG_USER_ID
        else:
            chat_id = event.user.telegramm_id

        return self.view.send_message(chat_id, event)

    def get_actual_timers(self):
        now = datetime.now()
        event_timers = session.query(EventTimer).filter(
            (EventTimer.send_time <= now) & (now < EventTimer.stop_time)
        ).all()
        print(event_timers)
        return event_timers

    def get_events_for_timer(self, event_timer: EventTimer):
        return session.query(Event).filter(Event.timer_id == event_timer.id).all()

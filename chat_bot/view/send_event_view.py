from chat_bot.models import Event


class SendEventView:
    def __init__(self, bot):
        self.bot = bot

    def send_message(self, chat_id, event: Event):
        event_type = event.event_type
        timer = event.timer
        msg = f'''{event_type.name}
с {timer.start_time} до {timer.stop_time}
по адресу {event_type.address.name}'''
        return self.bot.send_message(chat_id=chat_id, text=msg)

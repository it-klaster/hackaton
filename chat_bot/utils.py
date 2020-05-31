import inspect
import logging
from functools import wraps

import requests
from telegram import ChatAction


def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_method(self, update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(self, update, context,  *args, **kwargs)

    return command_method



def get_logging():
    logger = logging.getLogger()
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    return logger


def normalize_adrs(str) -> str:
    return ' '.join(str.split()).lower()


def find_address(latitude: float, longitude: float):
    geocoder_url = f'http://api.aigeo.ru/geocoder/service?search={latitude},{longitude}&format=json'
    resp = requests.get(url=geocoder_url)
    resp.raise_for_status()
    parsed_resp = resp.json()
    return parsed_resp['response']['results'][0]['fulladdressstring']

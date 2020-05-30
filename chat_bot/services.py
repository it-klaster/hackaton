import codecs
import json

from chat_bot.models import session, Event, EventType, EventTimer, Address
from datetime import datetime

from chat_bot.utils import get_logging

logger = get_logging()

def search_address(msg) -> list:
    adr = session.query(Address).filter(Address.name.ilike(f'{msg}%')).all()
    return adr

def get_user(telegramm_user_id):
    with codecs.open('resources/users.json', 'r+', encoding='utf-16') as json_file:
        users = json.loads(json_file.read())
        users = [user for user in users if user.get('telegramm_id') == telegramm_user_id]
        return users[0] if len(users) > 0 else None


def register_user(user):
    existing_user = get_user(user['telegramm_id'])
    if not existing_user:
        existing_user = user
    existing_user['address'] = user['address']

    with codecs.open('resources/users.json', 'r', encoding='utf-16') as json_file:
        users = json.loads(json_file.read())
        if not users:
            users = []
        users.append(existing_user)

    with codecs.open('resources/users.json', 'w', encoding='utf-16') as json_file:
        json_file.write(json.dumps(users))

    return existing_user


def get_events(adress_id):
    events = session.query(EventType, Event, EventTimer).filter(
        EventType.address_id == adress_id
    ).filter(
        EventTimer.start_time < datetime.now()
    ).filter(
        EventTimer.stop_time > datetime.now()
    ).all()
    return [e[0] for e in events]
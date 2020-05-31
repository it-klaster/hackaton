
from datetime import datetime

from chat_bot.models import session, Event, EventType, EventTimer, Address, User
from chat_bot.utils import get_logging

logger = get_logging()

def search_address(msg) -> list:
    adr = session.query(Address).filter(Address.name.ilike(f'{msg}%')).all()
    return adr

def get_user(telegramm_user_id):
    return session.query(User).filter(User.telegramm_id == telegramm_user_id).first()

def register_user(data):
    user = session.query(User).filter(User.telegramm_id == data['telegramm_id']).first()
    adr = search_address(data['address'])[0]
    if not user:
        name = f"{data['first_name']}"
        user = User(name=name, address_id=adr.id)

    user.telegramm_id = data['telegramm_id']

    session.add(user)
    session.commit()
    return user


def get_events(adress_id):
    events = session.query(EventType, Event, EventTimer).filter(
        EventType.address_id == adress_id
    ).filter(
        EventTimer.start_time < datetime.now()
    ).filter(
        EventTimer.stop_time > datetime.now()
    ).all()
    return [e[0] for e in events]
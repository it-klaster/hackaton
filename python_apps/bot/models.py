import textwrap

from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base

from settings import Config


engine = create_engine(Config.DB_URI, echo=True)

_SessionFactory = sessionmaker(bind=engine)
session = Session(engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'bot_users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    telegramm_id = Column(String, nullable=False, unique=True)
    address_id = Column(Integer, ForeignKey('bot_addreses.id'))
    entrance = Column(Integer)  # Not exist in db
    subscribe = Column(TINYINT(1))
    phone = Column(String)

    def __repr__(self):
        return f'<User {self.telegramm_id}>'


class Address(Base):
    __tablename__ = 'bot_addreses'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

    def __repr__(self):
        return f'<Address {self.name}>'


class Event(Base):
    __tablename__ = 'bot_events'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('bot_users.id'))
    event_id = Column(Integer, ForeignKey('bot_idevents.id'))
    timer_id = Column(Integer, ForeignKey('bot_etimer.id'))

    def __repr__(self):
        short_msg = textwrap.shorten(self.name, width=50, placeholder="...")
        return f'<Event {short_msg}>'


class EventType(Base):
    __tablename__ = 'bot_idevents'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # alert_id = Column(Integer, ForeignKey())
    status_id = Column(Integer, ForeignKey('bot_estatus.id'))
    address_id = Column(Integer, ForeignKey('bot_addreses.id'))


class MsgLog(Base):
    __tablename__ = 'bot_msglog'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('bot_users.id'))
    mag_text = Column(String)


class AdminUser(Base):
    __tablename__ = 'bot_admins'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    telegramm_id = Column(Integer, nullable=False, unique=True)
    org_id = Column(Integer, ForeignKey('bot_org.id'))
    rules_id = Column(Integer, ForeignKey('bot_rules.id'))


class Organization(Base):
    __tablename__ = 'bot_org'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Rules(Base):
    __tablename__ = 'bot_rules'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('bot_idevents.id'))
    organization_id = Column(Integer, ForeignKey('bot_org.id'))


class EventLog(Base):
    __tablename__ = 'bot_elog'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('bot_idevents.id'))
    operator_id = Column(Integer)   # TODO: Foreignkey


class EventStatus(Base):
    __tablename__ = 'bot_estatus'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class EventTimer(Base):
    __tablename__ = 'bot_etimer'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_time = Column(DateTime)
    stop_time = Column(DateTime)
    send_time = Column(DateTime)
    repeat = Column(TINYINT(1))


class EventWeight(Base):
    __tablename__ = 'bot_eweight'

    id = Column(Integer, primary_key=True)
    name = Column(String)

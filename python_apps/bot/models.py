import textwrap

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base

from settings import Config


engine = create_engine(Config.DB_URI, echo=True)

_SessionFactory = sessionmaker(bind=engine)
session = Session(engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegramm_id = Column(String, nullable=False, unique=True)
    address_id = Column(Integer, ForeignKey('addresses.id'))
    entrance = Column(Integer)

    def __repr__(self):
        return f'<User {self.telegramm_id}>'


class Address(Base):
    __tablename__ = 'addresses'
    __table_args__ = (
        UniqueConstraint('street', 'house'),
    )

    id = Column(Integer, primary_key=True)
    street = Column(String(256), nullable=False)
    house = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<Address {self.street}, {self.house}>'


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    msg = Column(String, nullable=False)
    importance = Column(Integer)
    start_date = Column(DateTime, nullable=False)
    finish_date = Column(DateTime)

    def __repr__(self):
        short_msg = textwrap.shorten(self.msg, width=50, placeholder="...")
        return f'<Event {self.start_date} {short_msg}>'


class SentEvent(Base):
    __tablename__ = 'sent_events_log'

    id = Column(Integer, primary_key=True)
    sent_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    event_id = Column(Integer, ForeignKey('events.id'))

    def __repr__(self):
        return f'<SentEvent {self.sent_at} {self.user}>'

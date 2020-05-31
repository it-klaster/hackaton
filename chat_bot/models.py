import textwrap

from settings import Config
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine(Config.DB_URI, echo=True)

_SessionFactory = sessionmaker(bind=engine)
session = Session(engine)

# TODO: change in prod
session.expire_on_commit = False

Base = declarative_base()


class User(Base):
    __tablename__ = 'bot_users'

    id = Column('ID', Integer, primary_key=True)
    name = Column('Name', String)
    telegramm_id = Column('TelegrammID', String, nullable=False, unique=True)
    address_id = Column('AddressID', Integer, ForeignKey('bot_addreses.ID'))
    # entrance = Column(Integer)  # Not exist in db
    subscribe = Column('Subscribe', TINYINT(1))
    phone = Column('Phone', String)

    address = relationship('Address', back_populates="users")

    def __repr__(self):
        return f'<User {self.telegramm_id}>'


class Address(Base):
    __tablename__ = 'bot_addreses'

    id = Column('ID', Integer, primary_key=True)
    name = Column('NAME', String(256), nullable=False)

    users = relationship("User")

    def __repr__(self):
        return f'<Address {self.name}>'


class Event(Base):
    __tablename__ = 'bot_events'

    id = Column('ID', Integer, primary_key=True)
    name = Column('Name', String, nullable=False)
    user_id = Column('UserID', Integer, ForeignKey('bot_users.ID'))
    event_id = Column('EventID', Integer, ForeignKey('bot_idevents.Id'))
    timer_id = Column('TimerID', Integer, ForeignKey('bot_etimer.ID'))
    send_at = Column('SendAt', DateTime, default=None)

    user = relationship('User')
    timer = relationship('EventTimer', backref='events')
    event_type = relationship('EventType')


class EventType(Base):
    __tablename__ = 'bot_idevents'

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String, nullable=False)
    alert_id = Column('AlertID', Integer)   # TODO: Foreignkey
    status_id = Column('StatusID', Integer, ForeignKey('bot_estatus.Id'))
    address_id = Column('AdrID', Integer, ForeignKey('bot_addreses.ID'))

    address = relationship('Address')

    def __repr__(self):
        short_msg = textwrap.shorten(self.name, width=50, placeholder="...")
        return f'<Event {short_msg}>'


class MsgLog(Base):
    __tablename__ = 'bot_msglog'

    id = Column('ID', Integer, primary_key=True)
    user_id = Column('UserID', Integer, ForeignKey('bot_users.id'))
    mag_text = Column('MagText', String)


class AdminUser(Base):
    __tablename__ = 'bot_admins'

    id = Column('ID', Integer, primary_key=True)
    name = Column('Name', String)
    telegramm_id = Column('TelegrammID', Integer, nullable=False, unique=True)
    org_id = Column('OrgID', Integer, ForeignKey('bot_org.id'))
    rules_id = Column('RulesID', Integer, ForeignKey('bot_rules.id'))


class Organization(Base):
    __tablename__ = 'bot_org'

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String)


class Rules(Base):
    __tablename__ = 'bot_rules'

    id = Column('Id', Integer, primary_key=True)
    event_id = Column('EventId', Integer, ForeignKey('bot_idevents.id'))
    organization_id = Column('OrgID', Integer, ForeignKey('bot_org.id'))


class EventLog(Base):
    __tablename__ = 'bot_elog'

    id = Column('ID', Integer, primary_key=True)
    event_id = Column('EventID', Integer, ForeignKey('bot_idevents.id'))
    operator_id = Column('OperatorID', Integer)   # TODO: Foreignkey


class EventStatus(Base):
    __tablename__ = 'bot_estatus'

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String)


class EventTimer(Base):
    __tablename__ = 'bot_etimer'

    id = Column('ID', Integer, primary_key=True)
    name = Column('Name', String)
    start_time = Column('StartTime', DateTime)
    stop_time = Column('StopTime', DateTime)
    send_time = Column('SendTime', DateTime)
    repeat = Column('Repeat', TINYINT(1))


class EventWeight(Base):
    __tablename__ = 'bot_eweight'

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String)

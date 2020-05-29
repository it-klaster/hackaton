import textwrap

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()
Base.metadata.create_all(engine)


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
        UniqueConstraint('street', 'house')
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
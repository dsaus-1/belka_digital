from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import FLOAT
from sqlalchemy.orm import validates


class Base(DeclarativeBase):
    pass

class General(Base):
    __tablename__ = 'general'

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DateTime)
    value = Column(FLOAT)

    @validates("value")
    def validate_value(self, key, value):
        if value > 10.0:
            raise ValueError("value greater than 10")

        elif value < 0.0:
            raise ValueError("value less than 0")
        return value


class DateMaxValue(Base):
    __tablename__ = 'datemaxvalue'

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DateTime)
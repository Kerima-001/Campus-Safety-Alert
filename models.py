from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    full_name = Column(String)

    email = Column(String, unique=True)

    password = Column(String)

    role = Column(String)

class Incident(Base):

    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    description = Column(String)

    severity = Column(String)

    latitude = Column(Float)

    longitude = Column(Float)

    image_url = Column(String)

    status = Column(String)

class Alert(Base):

    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    message = Column(String)

    alert_type = Column(String)

    target_area = Column(String)

    created_at = Column(DateTime)

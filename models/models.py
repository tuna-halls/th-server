import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import JSON
from sqlalchemy.ext.declarative import declarative_base

from .enums import HallState
from .enums import HallSecurityMode
from .enums import HallLogMode
from .enums import FeatureType
from .enums import Role
from .enums import Presence

import os

db_engine = os.environ.get("DB_ENGINE", "sqlite:///:memory:")

engine = create_engine(db_engine, echo=True)
Base = declarative_base()



class TimestampedMixin(object):
	created_at = Column(DateTime, default=datetime.now)
	updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class User(TimestampedMixin, Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key=True)
	email = Column(String, unique=True)
	password = Column(String)
	display_name = Column(String)
	profile_image = Column(String)
	member = relationship("HallMember", back_populates="user")


hallfeature_hall_association = Table('hallfeature_hall', Base.metadata,
    Column('hall_id', Integer, ForeignKey('hall.id')),
    Column('hallfeature_id', Integer, ForeignKey('HallFeature.id'))
)


hallmember_hall_association = Table('hallmember_hall', Base.metadata,
    Column('hall_id', Integer, ForeignKey('hall.id')),
    Column('hallmember_id', Integer, ForeignKey('hallmember.id'))
)


class Hall(TimestampedMixin, Base):
	__tablename__ = "hall"
	id = Column(Integer, primary_key=True)
	email = Column(String, unique=True)
	slug = Column(String)
	state = Column(Enum(HallState))
	title = Column(String)
	description = Column(String)
	profile_image = Column(String)
	security_mode = Column(Enum(HallSecurityMode))
	log_mode = Column(Enum(HallLogMode))
	share_link = Column(String)
	expires_at = Column(DateTime)
	features = relationship("HallFeature", secondary=hallfeatures_halls_association)
	members = relationship("HallMember", secondary=hallmember_hall_association)


class HallFeature(TimestampedMixin, Base):
	__tablename__ = "hallfeature"
	id = Column(Integer, primary_key=True)
	feature_type = Column(Enum(FeatureType))
	settings = Column(JSON)



class HallMember(TimestampedMixin, Base):
	__tablename__ = "hallmember"
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
	presence = Column(Enum(Presence))
	display_name = Column(String)
	profile_image = Column(String)
	role = Column(Enum(Role))


Base.metadata.create_all(engine)

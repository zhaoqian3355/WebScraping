"""test the declarative Base class"""

from test import Base

from sqlalchemy import Column, Integer, String

class User(Base):
    """this is a entity"""

    __tablename__ = "users"

    id = Column(Integer, primart_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='s%', fullname='s%', password='s%')>" % (self.name, self.fullname, self.password)

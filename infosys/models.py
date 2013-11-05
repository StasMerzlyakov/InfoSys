#-*- coding: UTF-8 -*-

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


"""
  Классификатор адресообразующих элементов
"""
class Object(Base):
    __tablename__ = 'fiac_object'
    """ Глобальный уникальный идентификатор адресного объекта  """
    aoguid = Column(Text, primary_key=True)



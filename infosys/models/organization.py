#-*- coding: UTF-8 -*-

from base import Base

from sqlalchemy import (
    Column,
    BigInteger,
    Integer,
    String,
    Text,
    Date,
    Boolean
    )


from sqlalchemy.schema import ForeignKey


"""
  Модель данных описывающая организацию
"""

class Organization(Base):

    __tablename__ = 'ORG_Organization'

    """ Идентификатор """
    id = Column(BigInteger, primary_key=True)

    """ Название """
    name = Column(String(length=60), nullable=False)

    """ Краткое описание деятельности """
    shorinfo = Column(String(length=250), nullable=False)

    """ Контактная информация """
    contactinfo = Column(String(length=100), nullable=False)




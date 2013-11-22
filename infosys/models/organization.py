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

    """ Наименовение """
    fullname = Column(String(length=20), nullable=False)

    """ Краткое наименование """
    shortname = Column(String(length=20), nullable=False, index=True)

    """ Префикс наименования организации (ЗАО, ОАО, ООО и т.д.)"""
    prefix = Column(String(length=10))

    """ Краткая информация о роде деятельности """
    shortinfo = Column(String(length=50), nullable=False)

    """ Описание рода дейтельности """
    funllinfo = Column(Text)

    """ Контактная информация """
    contact = Column(Text)




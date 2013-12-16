#-*- coding: UTF-8 -*-

from base import Base

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Boolean,
    Date
    )


from sqlalchemy.schema import ForeignKey


"""
  Коды ОКП
"""
class OKP(Base):

    __tablename__ = 'CL_OKP'

    """ Идентификатор """
    id = Column(Integer, primary_key=True, autoincrement=False)

    """ Наименовение """
    name = Column(String(length=300), nullable=False, index=True)

    """ Код ОКP """
    code = Column(String(length=50), nullable=False, index=True)

    """ Ссылка на родителя """
    pid = Column(Integer, ForeignKey('CL_OKP.id'), nullable=True, index=True)

    """ Код ОКP родителя """
    pcode = Column(String(length=50), nullable=True, index=True)

    """ Уровень вложенности """
    level = Column(Integer, nullable=False)

    """ Статус активности """
    active = Column(Boolean, nullable=False)

    """ Дата обновления записи """
    updateDate = Column(Date, nullable=False)


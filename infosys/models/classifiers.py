#-*- coding: UTF-8 -*-

from base import Base

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    )


from sqlalchemy.schema import ForeignKey


"""
  Коды ОКП
"""

class OKP(Base):

    __tablename__ = 'Classifiers_OKP'

    """ Идентификатор """
    id = Column(Integer, primary_key=True)

    """ Наименовение """
    name = Column(String(length=60), nullable=False, index=True)

    """ Код ОКP """
    code = Column(String(length=50), nullable=False, index=True)

    """ Ссылка на родителя """
    pid = Column(Integer, ForeignKey('Classifiers_OKP.id'), nullable=True)

    """ Уровень вложенности """
    level = Column(Integer, nullable=False)




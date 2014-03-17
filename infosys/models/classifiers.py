#-*- coding: UTF-8 -*-

from infosys.models.base import Base

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date
    )


from sqlalchemy.schema import ForeignKey


"""
  Код ОКП
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



"""
  Классификатор регионов.
"""
class Region(Base):
    __tablename__='CL_Region'

    """ Идентификатор """
    id = Column(Integer, primary_key=True, autoincrement=False)

    """ Наименование """
    name = Column(String(length=300), nullable=False, index=True)

    """ Ссылка на родителя """
    pid = Column(Integer, ForeignKey('CL_Region.id'), nullable=True, index=True)

    """ Уровень вложенности """
    level = Column(Integer, nullable=False)

    """ Флаг, указывющий есть ли потомки у узла """
    isParent = Column(Boolean, nullable=False)

    """ Статус активности """
    active = Column(Boolean, nullable=False)





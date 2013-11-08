#-*- coding: UTF-8 -*-

from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Text,
    Date,
    Boolean
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
    __tablename__ = 'FIAC_Object'
    """ Глобальный уникальный идентификатор адресного объекта  """
    """ HINT !!! """
    aoguid = Column(String(length=36),unique=True, nullable=False)

    """ Формализованное наименование """    
    formalname = Column(String(length=120), nullable=False)

    """ Код региона """
    regioncode = Column(String(length=2), nullable=False)

    """ Код автономии """
    autocode = Column(String(length=1), nullable=False)

    """ Код района """
    areacode = Column(String(length=3), nullable=False)

    """ Код города """
    citycode = Column(String(length=3), nullable=False)

    """ Код внутригородского района """
    ctarcode = Column(String(length=3), nullable=False)

    """ Код населенного пункта """
    placecode = Column(String(length=3), nullable=False)

    """ Код улицы """
    streetcode = Column(String(length=4), nullable=False)

    """ Код дополнительного адресообразующего элемента """
    extrcode = Column(String(length=4), nullable=False)

    """ Код подчиненного дополнительного адресообразующего элемента """
    sextcode = Column(String(length=3))

    """ Официальное наименование """
    offname = Column(String(length=120))

    """ Почтовый индекс """
    postalcode=Column(String(length=6))

    """ Код ИФНС ФЛ """
    ifnsfl = Column(String(length=4))

    """ Код территориального участка ИФНС ФЛ """
    terrifnsfl = Column(String(length=4))

    """ Код ИФНС ЮЛ """
    ifnsul = Column(String(length=4))

    """ Код территориального участка ИФНС ЮЛ """
    terrifnsul = Column(String(length=4))

    """ ОКАТО """
    okato = Column(String(length=11))

    """ ОКТМО """
    oktmo = Column(String(length=8))

    """ Дата  внесения (обновления) записи """
    updatedate = Column(Date,nullable=False)

    """ Краткое наименование типа объекта """
    shortname = Column(String(length=10),nullable=False)

    """ Уровень адресного объекта """
    aolevel = Column(Integer,nullable=False)

    """ Идентификатор объекта родительского объекта """
    """ HINT !!! """
    parentguid = Column(String(length=36)) 

    """ Уникальный идентификатор записи. Ключевое поле. """
    """ HINT !!! """
    aoid = Column(String(length=36),primary_key=True)

    """ Идентификатор записи связывания с предыдушей исторической записью """
    """ HINT !!! """
    previd = Column(String(length=36))

    """ Идентификатор записи  связывания с последующей исторической записью """
    """ HINT !!! """
    nextid = Column(String(length=36))

    """ Код адресного объекта одной строкой с признаком актуальности из КЛАДР 4.0. """
    code = Column(String(length=17))

    """ Код адресного объекта из КЛАДР 4.0 одной строкой без признака актуальности (последних двух цифр)"""
    plaincode = Column(String(length=15))

    """ Статус актуальности адресного объекта ФИАС. 
        Актуальный адрес на текущую дату. 
        Обычно последняя запись об адресном объекте.
         0 – Не актуальный
         1 - Актуальный """
    actstatus = Column(Integer, nullable=False)

    """ Статус центра """
    centstatus = Column(Integer, nullable=False)

    """ Статус действия над записью – причина появления записи (см OperationStatus) """
    operstatus = Column(Integer, nullable=False)

    """ Статус актуальности КЛАДР 4 (последние две цифры в коде) """
    currstatus = Column(Integer, nullable=False)

    """ Начало действия записи """
    startdate = Column(Date, nullable=False)

    """ Окончание действия записи """
    enddate = Column(Date, nullable=False)

    """ Внешний ключ на нормативный документ"""
    """ HINT !!!!"""
    normdoc = Column(String(length=36))

    """ Признак действующего адресного объекта """
    livestatus=Column(Boolean, nullable=False)



""" Сведения по номерам домов улиц городов и населенных пунктов, номера земельных участков и т.п """
class House(Base):
    __tablename__ = 'FIAC_House'
    """ Почтовый индекс """
    postalcode = Column(String(length=6))

    """ Код ИФНС ФЛ """
    ifnsfl = Column(String(length=4))

    """ Код территориального участка ИФНС ФЛ """
    terrifsnfl = Column(String(length=4))
   
    """ Код ИФНС ЮЛ """
    ifnsul = Column(String(length=4))

    """ Код территориального участка ИФНС ЮЛ """
    terrifnsul = Column(String(length=4))

    """ ОКАТО """
    okato = Column(String(length=11))
   
    """ ОКТМО """
    oktmo = Column(String(length=8))

    """ Дата время внесения записи """
    updatedate = Column(Date, nullable=False)

    """ Номер дома """
    housenum = Column(String(length=20))

    """ Признак владения """
    eststatus = Column(Integer, nullable=False)

    """ Номер корпуса """
    buildnum = Column(String(length=10))

    """ Номер строения """
    strucnum = Column(String(length=10))

    """ Признак строения """
    strstatus = Column(Integer)

    """ Уникальный идентификатор записи дома """
    """ HINT !!! """
    houseid = Column(String(length=36), primary_key=True)
  
    """ Глобальный уникальный идентификатор дома """
    """ HINT !!! """
    houseguid = Column(String(length=36), unique=True, nullable=False)

    """ Guid записи родительского объекта (улицы, города, населенного пункта и т.п.) """
    """ HINT !!! """
    aoguid = Column(String(length=36), nullable=False)

    """ Начало действия записи """
    startdate = Column(Date, nullable=False)

    """ Окончание действия записи """
    enddate = Column(Date, nullable=False)
 
    """ Состояние дома """
    statstatus  = Column(Integer, nullable=False)   
   
    """ Внешний ключ на нормативный документ """
    """ HINT !!! """
    normdoc = Column(String(length=36))
 
    """ Счетчик записей домов для КЛАДР 4 """
    counter = Column(Integer, nullable=False)    

 

""" Интервалы домов """
class HouseInterval(Base):
    __tablename__ = 'FIAC_HouseInterval'

    """ Почтовый индекс """
    postalcode = Column(String(length=6))

    """ Код ИФНС ФЛ """
    ifnsfl = Column(String(length=4))

    """ Код территориального участка ИФНС ФЛ """
    terrifsnfl = Column(String(length=4))
   
    """ Код ИФНС ЮЛ """
    ifnsul = Column(String(length=4))

    """ Код территориального участка ИФНС ЮЛ """
    terrifnsul = Column(String(length=4))

    """ ОКАТО """
    okato = Column(String(length=11))

    """ ОКТМО """
    oktmo = Column(String(length=8))

    """ Дата  внесения (обновления) записи """
    updatedate = Column(Date, nullable=False)
  
    """ Значение начала интервала """
    intstart = Column(Integer, nullable=False)   
   
    """ Значение окончания интервала """
    intend = Column(Integer,nullable=False)

    """ Идентификатор записи интервала домов """
    """ HINT !!! """
    houseintid = Column(String(length=36), primary_key=True)

    """ Глобальный уникальный идентификатор интервала домов """
    """ HINT !!! """
    intguid = Column(String(length=36), unique=True, nullable=False)

    """ Идентификатор объекта родительского объекта (улицы, города, населенного пункта и т.п.) """
    """ HINT !!! """
    aoguid = Column(String(length=36), nullable=False)

    """ Начало действия записи """
    startdate = Column(Date, nullable=False)

    """ Окончание действия записи """
    enddate = Column(Date, nullable=False)
     
    """ Внешний ключ на нормативный документ """
    """ HINT !!! """
    normdoc = Column(String(length=36))
 
    """ Счетчик записей домов для КЛАДР 4 """
    counter = Column(Integer, nullable=False)




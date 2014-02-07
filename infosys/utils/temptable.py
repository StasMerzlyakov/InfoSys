# -*- coding: utf-8 -*-

import uuid
from sqlalchemy.dialects.postgresql import array

from sqlalchemy.types import BigInteger, Integer, CHAR
from sqlalchemy import Column, MetaData, Table
from infosys import engine
from sqlalchemy.sql.expression import Executable, ClauseElement
from sqlalchemy.ext.compiler import compiles
from sqlalchemy import func
from sqlalchemy.sql import  select

metadata = MetaData()

#
# Смотрим что предлагают умные люди.
# http://andrewgrossmanatwork.blogspot.ru/2012/12/postgres-temporary-table-definition-and.html
#
class InsertFromSelect(Executable, ClauseElement):
  def __init__(self, table, select):
    self.table = table
    self.select = select

@compiles(InsertFromSelect)
def visit_insert_from_select(element, compiler, **kw):
  return "INSERT INTO %s select * from unnest(array %s ::sphinx_search_result[])" % (
   compiler.process(element.table, asfrom=True),
   element.select
  )

#
# Создаем временную таблицу
#
def create_temp_table(session, insert_list):
  table_name = "temp_" + str(uuid.uuid1()).replace("-", '')

  temp_table = Table(table_name, metadata,
  Column('id', BigInteger,primary_key=True),
  Column('weight', Integer),
  prefixes=['TEMPORARY']
  )

  temp_table.create(bind=session.bind)

  insert_statement = InsertFromSelect(temp_table, insert_list)

  session.execute(insert_statement)

  return temp_table
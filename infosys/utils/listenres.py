# -*- coding: utf-8 -*-

#
# Добавляем нужные листенеры
#

from sqlalchemy import event

from sqlalchemy.pool import Pool
from psycopg2.extras import register_composite


@event.listens_for(Pool, 'connect')
def receive_connect(dbapi_connection, connection_record):
  pass
  #register_composite('sphinx_search_result', dbapi_connection)

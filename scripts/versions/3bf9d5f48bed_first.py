#-*- coding: UTF-8 -*-
"""first

Revision ID: 3bf9d5f48bed
Revises: None
Create Date: 2013-11-05 15:52:19.254290

Первая ревизия.
Начал описывать модель FIAC.Object.
( Классификатор адресообразующих элементов).

"""

# revision identifiers, used by Alembic.
revision = '3bf9d5f48bed'
down_revision = None

from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql import table,column

from sqlalchemy import (
    Column,
    Text
)


def upgrade():
    # Создаем таблицу Object
    op.create_table(
      'fiac_object',
      Column('aoguid',Text, primary_key=True),
    )


def downgrade():
    # Удаляем таблицу Object
    op.drop_table('fiac_object')

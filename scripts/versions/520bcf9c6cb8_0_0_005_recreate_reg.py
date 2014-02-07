#-*- coding: UTF-8 -*-

"""

0.0.005_recreate_region

Revision ID: 520bcf9c6cb8
Revises: 462a91ed51ac
Create Date: 2013-12-24 10:55:09.072136

Пересоздание таблицы регионов

"""

# revision identifiers, used by Alembic.
revision = '520bcf9c6cb8'
down_revision = '462a91ed51ac'

from alembic import op

from sqlalchemy import (
  Column,
  Integer,
  String,
  ForeignKey,
  Boolean,
)
 
def upgrade():
    op.drop_table('CL_Region')
    op.create_table('CL_Region',
    Column('id',Integer, primary_key=True, autoincrement=False),
    Column('name',String(length=300), nullable=False, index=True),
    Column('pid',Integer, ForeignKey('CL_Region.id'), nullable=True, index=True),
    Column('level',Integer, nullable=False),
    Column('isParent',Boolean, nullable=False),
    Column('active',Boolean, nullable=False)
  )



def downgrade():
    op.drop_table('CL_Region')
    op.create_table('CL_Region',
    Column('id',Integer, primary_key=True, autoincrement=False),
    Column('name',String(length=300), nullable=False, index=True),
    Column('pid',Integer, ForeignKey('CL_Region.id'), nullable=True, index=True),
    Column('level',Integer, nullable=False),
    Column('active',Boolean, nullable=False)
)



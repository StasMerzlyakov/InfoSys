#-*- coding: UTF-8 -*-
"""first

Revision ID: 3bf9d5f48bed
Revises: None
Create Date: 2013-11-05 15:52:19.254290

Первая ревизия.
Модель данных ФИАС
( Классификатор адресообразующих элементов).

"""

# revision identifiers, used by Alembic.
revision = '3bf9d5f48bed'
down_revision = None

from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql import table


from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Text,
    Date,
    Boolean
    )



def upgrade():
    op.create_table(
    'FIAS_Object',
    Column('aoguid', String(length=36), unique=True, nullable=False),
    Column('formalname', String(length=120), nullable=False),
    Column('regioncode',String(length=2), nullable=False),
    Column('autocode',String(length=1), nullable=False),
    Column('areacode',String(length=3), nullable=False),
    Column('citycode', String(length=3), nullable=False),
    Column('ctarcode', String(length=3), nullable=False),
    Column('placecode',String(length=3), nullable=False),
    Column('streetcode', String(length=4), nullable=False),
    Column('extrcode', String(length=4), nullable=False),
    Column('sextcode', String(length=3)),
    Column('offname', String(length=120)),
    Column('postalcode', String(length=6)),
    Column('ifnsul', String(length=4)),
    Column('terrifnsul', String(length=4)),
    Column('ifnsul', String(length=4)),
    Column('terrifnsul', String(length=4)),
    Column('okato', String(length=11)),
    Column('oktmo', String(length=8)),
    Column('updatedate', Date,nullable=False),
    Column('shortname', String(length=10),nullable=False),
    Column('aolevel', Integer,nullable=False),
    Column('parentguid', String(length=36)),
    Column('aoid', String(length=36),primary_key=True),
    Column('previd', String(length=36)),
    Column('nextid', String(length=36)),
    Column('code', String(length=17)),
    Column('plaincode',String(length=15)),
    Column('actstatus', Integer, nullable=False),
    Column('centstatus', Integer, nullable=False),
    Column('operstatus', Integer, nullable=False),
    Column('currstatus', Integer, nullable=False),
    Column('startdate', Date, nullable=False),
    Column('enddate', Date, nullable=False),
    Column('normdoc', String(length=36)),
    Column('livestatus',Boolean, nullable=False),

    )


    op.create_table(
    'FIAS_House',
    Column('postalcode', String(length=6)),
    Column('ifnsul', String(length=4)),
    Column('terrifnsul', String(length=4)),
    Column('ifnsul', String(length=4)),
    Column('terrifnsul', String(length=4)),
    Column('okato', String(length=11)),
    Column('oktmo', String(length=8)),
    Column('updatedate', Date, nullable=False),
    Column('housenum', String(length=20)),
    Column('eststatus', Integer, nullable=False),
    Column('buildnum', String(length=10)),
    Column('strucnum', String(length=10)),
    Column('strstatus', Integer),
    Column('houseid', String(length=36), primary_key=True),
    Column('houseguid', String(length=36), unique=True, nullable=False),
    Column('aoguid', String(length=36), nullable=False),
    Column('startdate', Date, nullable=False),
    Column('enddate', Date, nullable=False),
    Column('statstatus', Integer, nullable=False),
    Column('normdoc', String(length=36)),
    Column('counter', Integer, nullable=False),
    )

    op.create_table(
    'FIAS_HouseInterval',
    Column('postalcode', String(length=6)),
    Column('ifnsul', String(length=4)),
    Column('terrifnsul', String(length=4)),
    Column('ifnsul', String(length=4)),
    Column('terrifnsul', String(length=4)),
    Column('okato', String(length=11)),
    Column('oktmo', String(length=8)),
    Column('updatedate', Date, nullable=False),
    Column('intstart', Integer, nullable=False),
    Column('intend', Integer,nullable=False),
    Column('houseintid', String(length=36), primary_key=True),
    Column('intguid', String(length=36), unique=True, nullable=False),
    Column('aoguid', String(length=36), nullable=False),
    Column('startdate', Date, nullable=False),
    Column('enddate', Date, nullable=False),
    Column('statstatus', Integer, nullable=False),
    Column('normdoc', String(length=36)),
    Column('counter', Integer, nullable=False),
    ) 

    op.create_table(
    'FIAS_Landmark',
    Column('location', String(length=500), nullable=False),
    Column('postalcode', String(length=6)),
    Column('ifnsul', String(length=4)),
    Column('terrifnsul', String(length=4)),
    Column('ifnsul', String(length=4)),
    Column('terrifnsul', String(length=4)),
    Column('okato', String(length=11)),
    Column('oktmo', String(length=8)),
    Column('updatedate', Date, nullable=False),
    Column('landid',String(length=36), primary_key=True),
    Column('landguid',String(length=36), unique=True, nullable=False),
    Column('aoguid', String(length=36), nullable=False),
    Column('startdate', Date, nullable=False),
    Column('enddate', Date, nullable=False),
    Column('statstatus', Integer, nullable=False),
    Column('normdoc', String(length=36)),
    )

    op.create_table(
    'FIAS_NormDoc',
    Column('normdocid',String(length=36), primary_key=True),
    Column('docname', String),
    Column('docdate',Date),
    Column('docnum', String(length=20)),
    Column('doctype', Integer,nullable=False),
    Column('docimgid', Integer, nullable=False)
    )

def downgrade():
    op.drop_table('FIAS_Object')
    op.drop_table('FIAS_House')
    op.drop_table('FIAS_HouseInterval')
    op.drop_table('FIAS_Landmark')
    op.drop_table('FIAS_NormDoc')






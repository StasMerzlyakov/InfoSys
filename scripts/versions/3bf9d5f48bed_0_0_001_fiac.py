#-*- coding: UTF-8 -*-
"""0.0.001_first

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

from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Text,
    Date,
    Boolean,
    ForeignKey
    )



def upgrade():
    op.create_table(
    'FIAS_AddressObjectType',
    Column('level', Integer, nullable=False),
    Column('scname', String(length=10)),
    Column('socrname', String(length=50),nullable=False),
    Column('kod_t_st', String(length=4), primary_key=True)
    )

    op.create_table(
    'FIAS_CurrentStatus',
    Column('curentstid', Integer, primary_key=True),
    Column('name', String(length=100), nullable=False)
    )

    op.create_table(
    'FIAS_ActualStatus',
    Column('actstatid', Integer, primary_key=True),
    Column('name', String(length=100),nullable=False)
    )

    op.create_table(
    'FIAS_OperationStatus',
    Column('operstatid', Integer, primary_key=True),
    Column('name', String(length=100),nullable=False)
    )
   
    op.create_table(
    'FIAS_CenterStatus',
    Column('centerstid', Integer, primary_key=True),
    Column('name', String(length=100),nullable=False)
    )
    
    op.create_table(
    'FIAS_IntervalStatus',
    Column('intvstatid', Integer, primary_key=True),
    Column('name', String(length=60),nullable=False)
    )
 
    op.create_table(
    'FIAS_HouseStateStatus',
    Column('housestid', Integer, primary_key=True),
    Column('name', String(length=60),nullable=False)
    )

    op.create_table(
    'FIAS_EstateStatus',
    Column('eststatid', Integer, primary_key=True),
    Column('name', String(length=20),nullable=False),
    Column('shortname', String(length=20),nullable=False)
    )

    op.create_table(
    'FIAS_StructureStatus',
    Column('strstatid', Integer, primary_key=True),
    Column('name', String(length=20),nullable=False),
    Column('shortname', String(length=20),nullable=False)
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
    Column('parentguid', String(length=36), ForeignKey('FIAS_Object.aoid')),
    Column('aoid', String(length=36),primary_key=True),
    Column('previd', String(length=36), ForeignKey('FIAS_Object.aoid'), nullable=True),
    Column('nextid', String(length=36), ForeignKey('FIAS_Object.aoid'), nullable=True),
    Column('code', String(length=17)),
    Column('plaincode',String(length=15)),
    Column('actstatus', Integer, ForeignKey('FIAS_ActualStatus.actstatid'), nullable=False),
    Column('centstatus', Integer, ForeignKey('FIAS_CenterStatus.centerstid'), nullable=False),
    Column('operstatus', Integer, ForeignKey('FIAS_OperationStatus.operstatid'), nullable=False),
    Column('currstatus', Integer, ForeignKey('FIAS_CurrentStatus.curentstid'), nullable=False),
    Column('startdate', Date, nullable=False),
    Column('enddate', Date, nullable=False),
    Column('normdoc', String(length=36), ForeignKey('FIAS_NormDoc.normdocid')),
    Column('livestatus', Boolean, nullable=False),
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
    Column('eststatus', Integer, ForeignKey('FIAS_EstateStatus.eststatid'), nullable=False),
    Column('buildnum', String(length=10)),
    Column('strucnum', String(length=10)),
    Column('strstatus', Integer, ForeignKey('FIAS_StructureStatus.strstatid')),
    Column('houseid', String(length=36), primary_key=True),
    Column('houseguid', String(length=36), unique=True, nullable=False),
    Column('aoguid', String(length=36), nullable=False),
    Column('startdate', Date, nullable=False),
    Column('enddate', Date, nullable=False),
    Column('statstatus', Integer, ForeignKey('FIAS_HouseStateStatus.housestid'), nullable=False),
    Column('normdoc', String(length=36), ForeignKey('FIAS_NormDoc.normdocid')),
    Column('counter', Integer, nullable=False)
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
    Column('normdoc', String(length=36), ForeignKey('FIAS_NormDoc.normdocid')),
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
    Column('normdoc', String(length=36), ForeignKey('FIAS_NormDoc.normdocid')),
    )


 
def downgrade():
    op.drop_table('FIAS_Object')
    op.drop_table('FIAS_House')
    op.drop_table('FIAS_HouseInterval')
    op.drop_table('FIAS_Landmark')
    op.drop_table('FIAS_NormDoc')
    op.drop_table('FIAS_AddressObjectType')
    op.drop_table('FIAS_CurrentStatus')
    op.drop_table('FIAS_ActualStatus')
    op.drop_table('FIAS_OperationStatus')
    op.drop_table('FIAS_CenterStatus')
    op.drop_table('FIAS_IntervalStatus')
    op.drop_table('FIAS_HouseStateStatus')
    op.drop_table('FIAS_EstateStatus')
    op.drop_table('FIAS_StructureStatus')   






#-*- coding: UTF-8 -*-
"""recreate_bd_0.0.006

Revision ID: 2d5ad06e90aa
Revises: 520bcf9c6cb8
Create Date: 2014-01-29 16:15:31.268915

Упрощение БД.

"""

# revision identifiers, used by Alembic.
revision = '2d5ad06e90aa'
down_revision = '520bcf9c6cb8'

from alembic import op

from sqlalchemy import (
    Column,
    BigInteger,
    String, 
    )



def upgrade():
    op.drop_table('CL_OKP')
    op.drop_table('CL_Region')
    op.drop_table('ORG_Organization')
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

    op.create_table(
    'ORG_Organization',
    Column('id', BigInteger, primary_key=True),
    Column('name', String(length=60), nullable=False),
    Column('shortinfo', String(length=500), nullable=False),
    Column('contactinfo', String(length=100), nullable=False))





def downgrade():
    # Обратная миграция не поддерживается.
    raise Exception('Обратная миграция не поддерживается')





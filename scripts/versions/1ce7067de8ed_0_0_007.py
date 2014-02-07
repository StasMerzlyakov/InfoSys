#-*- coding: UTF-8 -*-
"""0.0.007

Revision ID: 1ce7067de8ed
Revises: 2d5ad06e90aa
Create Date: 2014-01-30 12:29:03.018063

Переименовывание поля contactinfo в placeinfo

"""

# revision identifiers, used by Alembic.
revision = '1ce7067de8ed'
down_revision = '2d5ad06e90aa'

from alembic import op


def upgrade():
    op.alter_column('ORG_Organization','contactinfo',new_column_name='placeinfo')


def downgrade():
    op.alter_column('ORG_Organization','placeinfo',new_column_name='contactinfo')
    

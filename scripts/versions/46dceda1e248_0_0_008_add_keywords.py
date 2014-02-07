#-*- coding: UTF-8 -*-
"""0.0.008_add_keywords

Revision ID: 46dceda1e248
Revises: 1ce7067de8ed
Create Date: 2014-02-05 10:59:10.885862

Добавление поля "Ключевые слова" в таблиыу "Организация"

"""

# revision identifiers, used by Alembic.
revision = '46dceda1e248'
down_revision = '1ce7067de8ed'

from alembic import op

from sqlalchemy import (
    String, 
    Column
    )


def upgrade():
    op.add_column('ORG_Organization',Column('keywords', String(length=500), nullable=True))


def downgrade():
    op.drop_column('ORG_Organization','keywords')

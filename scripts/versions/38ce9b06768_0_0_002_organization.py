#-*- coding: UTF-8 -*-

"""0.0.002_organization

Revision ID: 38ce9b06768
Revises: 3bf9d5f48bed
Create Date: 2013-11-22 14:23:15.512167

Модель данных - Организация

"""

# revision identifiers, used by Alembic.
revision = '38ce9b06768'
down_revision = '3bf9d5f48bed'

from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql import table


from sqlalchemy import (
    Column,
    BigInteger,
    String, 
    Text,
    )


def upgrade():
    op.create_table(
    'ORG_Organization',
    Column('id', BigInteger, primary_key=True),
    Column('fullname', String(length=20), nullable=False),
    Column('shortname', String(length=20), nullable=False, index=True),
    Column('prefix', String(length=10)),
    Column('shortinfo', String(length=50), nullable=False),
    Column('fullinfo', Text),
    Column('contact', Text))


def downgrade():
    op.drop_table('ORG_Organization')



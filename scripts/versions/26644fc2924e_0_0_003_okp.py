#-*- coding: UTF-8 -*-
"""0.0.003_okp

Revision ID: 26644fc2924e
Revises: 38ce9b06768
Create Date: 2013-11-27 14:23:53.867408

Код ОКП

"""

# revision identifiers, used by Alembic.
revision = '26644fc2924e'
down_revision = '38ce9b06768'

from alembic import op
import sqlalchemy as sa

from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    ForeignKey
    )


def upgrade():
    op.create_table(
    'Classifiers_OKP',
    Column('id',Integer, primary_key=True),
    Column('name',String(length=60), nullable=False, index=True),
    Column('code',String(length=50), nullable=False, index=True),
    Column('pid',Integer, ForeignKey('Classifiers_OKP.id'), nullable=True),
    Column('level',Integer, nullable=False))

def downgrade():
    op.drop_table('Classifiers_OKP')


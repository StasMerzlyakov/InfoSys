#-*- coding: UTF-8 -*-
"""

0.0.004_regions

Revision ID: 462a91ed51ac
Revises: 26644fc2924e
Create Date: 2013-12-17 13:16:46.415506

Регионы

"""

# revision identifiers, used by Alembic.
revision = '462a91ed51ac'
down_revision = '26644fc2924e'


from alembic import op
import sqlalchemy as sa

from sqlalchemy import (
	  Column,
	  Index,
	  Integer,
	  String,
	  ForeignKey,
	  Boolean,
)
 
def upgrade():
    op.create_table(
    'CL_Region',
    Column('id',Integer, primary_key=True, autoincrement=False),
    Column('name',String(length=300), nullable=False, index=True),
    Column('pid',Integer, ForeignKey('CL_Region.id'), nullable=True, index=True),
    Column('level',Integer, nullable=False),
    Column('active',Boolean, nullable=False)
		)


def downgrade():
		op.drop_table('CL_Region')




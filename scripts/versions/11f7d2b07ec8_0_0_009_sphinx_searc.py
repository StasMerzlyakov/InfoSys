#-*- coding: UTF-8 -*-
"""0.0.009_sphinx_search_result

Revision ID: 11f7d2b07ec8
Revises: 46dceda1e248
Create Date: 2014-02-07 13:17:35.289845

Добавиление типа sphinx_search_result

"""

# revision identifiers, used by Alembic.
revision = '11f7d2b07ec8'
down_revision = '46dceda1e248'

from alembic import op
from sqlalchemy.sql import text


def upgrade():
  create_type_query = 'create type sphinx_search_result as (id bigint, weight int);'
  op.execute(text(create_type_query))


def downgrade():
  drop_type_query = 'drop type sphinx_search_result;'
  op.execute(text(drop_type_query))


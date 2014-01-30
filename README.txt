skyProject README
==================

Getting Started
---------------

- cd <directory containing this file>

- $venv/bin/python setup.py develop

- $venv/bin/initialize_skyProject_db development.ini

- $venv/bin/pserve development.ini

# Создать миграцию
- $venv/bin/alembic -c development.ini -n app:main revision -m "test"


# Обновить БД
# Пока offline
- $venv/bin/alembic -c development.ini -n app:main upgrade head

- $env/bin/alembic -c development.ini -n app:main downgrade -1




1. sphinxsearch
2. postgresql
3. pg-sphinx




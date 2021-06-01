#!/usr/bin/env bash

echo $(pwd)

ls ./blog

echo 'Removing blog migrations...'
find ./blog/migrations -name '*.py' -not -name '__init__.py' -delete
find ./blog/migrations -name '*.pyc' -delete

echo 'Removing info migrations...'
find ./info/migrations -name '*.py' -not -name '__init__.py' -delete
find ./info/migrations -name '*.pyc' -delete

echo 'Dropping and recreating database...'
psql -d postgres -c 'DROP DATABASE django;'

echo 'Recreating database...'
psql -d postgres -c $'CREATE DATABASE django WITH ENCODING = \'UTF8\' OWNER django;'

echo 'Recreating migrations...'
source ./venv/bin/activate
python ./manage.py makemigrations

echo 'Applying migrations...'
python ./manage.py migrate
deactivate
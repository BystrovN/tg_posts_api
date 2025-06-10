#!/bin/bash
python manage.py makemigrations

python manage.py migrate

python manage.py runserver &

python -m bot.bot

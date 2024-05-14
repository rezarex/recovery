@echo off

:: Apply database migrations
python manage.py migrate

:: Start the Daphne server
daphne -p 8000 datarecoverytool.asgi:application
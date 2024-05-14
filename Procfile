release: npm install && python manage.py migrate
web: npm run build && daphne -b 0.0.0.0 -p $PORT datarecoverytool.asgi:application

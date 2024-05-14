# Data Recovery Tool

This project is a web-based data recovery tool built with Django and Django Channels to support WebSockets.

## Requirements

- Python 3.7 or higher
- Django 3.x
- Channels 3.x
- Daphne 3.x

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/datarecoverytool.git
    cd datarecoverytool
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Run the server:**
    On Unix-like systems:
    ```sh
    ./run.sh
    ```
    On Windows:
    ```bat
    run.bat
    ```

6. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:8000
    ```

## Deployment

To deploy this app, you need to use a hosting service that supports ASGI applications. Some popular options are:

- **Heroku**
- **AWS Elastic Beanstalk**
- **DigitalOcean App Platform**

### Heroku Deployment Example

1. **Install the Heroku CLI:**
    Follow the instructions on the [Heroku CLI installation page](https://devcenter.heroku.com/articles/heroku-cli).

2. **Log in to Heroku:**
    ```sh
    heroku login
    ```

3. **Create a Heroku app:**
    ```sh
    heroku create your-app-name
    ```

4. **Add the Heroku Postgres addon:**
    ```sh
    heroku addons:create heroku-postgresql:hobby-dev
    ```

5. **Set environment variables:**
    ```sh
    heroku config:set DJANGO_SETTINGS_MODULE=datarecoverytool.settings.production
    ```

6. **Deploy the app:**
    ```sh
    git push heroku main
    ```

7. **Run database migrations:**
    ```sh
    heroku run python manage.py migrate
    ```

8. **Open the app in your browser:**
    ```sh
    heroku open
    ```

### Configuring ASGI on Heroku

1. **Add `Procfile` to the root of your project:**
    ```
    web: daphne -b 0.0.0.0 -p $PORT datarecoverytool.asgi:application
    ```

2. **Ensure all dependencies are listed in `requirements.txt`**

### Final Notes

When deploying the app, ensure that the hosting platform supports ASGI. The example above outlines how to set up and run the server both locally and on Heroku. Adjust the deployment steps according to your hosting provider if it differs from Heroku.

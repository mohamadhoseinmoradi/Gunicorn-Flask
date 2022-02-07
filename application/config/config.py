from os import environ


class config:

    ENV = environ.get("FLASK_ENV", default="production")
    DEBUG = bool(environ.get("FLASK_DEBUG", default=False))
    TESTING = bool(environ.get("FLASK_TESTING", default=False))

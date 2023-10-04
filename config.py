import os
from pydantic import BaseSettings
from apps.utils.custom_exceptions import ImproperlyConfigured


def get_from_env(key):
    try:
        return os.environ[key]
    except KeyError:
        error_message = f"Set the {key} environment variable"
        raise ImproperlyConfigured(error_message)

DEBUG = os.getenv("IS_DEV", True)

if DEBUG:
    min_level = 'DEBUG'
else:
    min_level = 'INFO'

APP_NAME = "be-admin-ecommerace-service"
LOGGER_NAME_PREFIX = f"{APP_NAME}."

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s  (%(name)s.%(funcName)s:%(lineno)d) - %(message)s"
        },
        'simple': {
            'format': "[%(asctime)s] %(levelname)s - %(message)s"
        },
    },
    'handlers': {
        'console': {
            'level': min_level,
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        APP_NAME: {
            'handlers': ['console'],
            'level': min_level,
            'propagate': False,
        },
        'uvicorn': {
            'handlers': ['console'],
            'level': min_level,
            'propagate': True,
        }
    },
}


class Settings(BaseSettings):
    app_name: str = APP_NAME
    logger_name_prefix = LOGGER_NAME_PREFIX
    logging_config = LOGGING


settings = Settings()

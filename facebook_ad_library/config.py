import os
try:
    from dotenv import dotenv_values

    config = {
        **dotenv_values(),
        **os.environ,
    }
except ImportError:
    config = {**os.environ}

FACEBOOK_TOKEN = config.get('FACEBOOK_TOKEN')
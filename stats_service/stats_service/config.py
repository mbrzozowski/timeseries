from os import getenv


APP_DEBUG = bool(getenv("APP_DEBUG", False))
APP_INTERFACE = getenv("APP_INTERFACE", "0.0.0.0")
APP_PORT = int(getenv("PORT", 8686))
DATABASE_URL = getenv("DATABASE_URL", "sqlite:///data.db")

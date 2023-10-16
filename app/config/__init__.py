import os

configuration = {
    "app": {
        "name": os.environ.get("APP_NAME", "app"),
        "version": os.environ.get("APP_VERSION", "0.0.1"),
        "environment": os.environ.get("APP_ENV", "development"),
    },
    "db": {
        "engine": os.environ.get("DB_ENGINE", "sqlite"),
        "host": os.environ.get("DB_HOST", "localhost"),
        "port": os.environ.get("DB_PORT", "5432"),
        "dbname": os.environ.get("DB_NAME", "postgres"),
        "user": os.environ.get("DB_USER", "postgres"),
        "password": os.environ.get("DB_PASSWORD", "postgres"),
    },
}

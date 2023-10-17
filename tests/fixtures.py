import pytest

from app.core import App
from app.core.db import drop_all_sync, migrate_sync


pytest_plugins = ("pytest_asyncio",)

test_config = {
    "app": {
        "name": "test",
        "version": "1.0.0",
        "environment": "test",
    },
    "db": {
        "engine": "postgres",
        "host": "postgresdb",
        "port": "5432",
        "dbname": "test",
        "user": "postgres",
        "password": "postgres",
    }
}


@pytest.fixture
def api():
    app = App(test_config)
    migrate_sync(drop_all=True)
    yield app
    drop_all_sync()

from loguru import logger

from app.config import configuration as app_config
from app.core.config import config
from app.core.logging import (
    LOG_LEVEL_INFO, LOG_LEVEL_WARNING, load_logging_handlers)


class App:
    config = config
    log = logger

    def __init__(self, configuration: dict = app_config):
        self.log.info("🚀 Initializing app...")
        self.setup_configuration(configuration)
        self.setup_logging()
        self.log.info("🤖 App initialized.")

    def setup_configuration(self, configuration: dict):
        self.log.info("⚙️  Setting up configuration...")
        self.config.load(configuration)

    def setup_logging(self):
        self.log.info("⚙️  Setting up logging...")
        log_level = LOG_LEVEL_INFO \
            if self.config.app.environment == "development" \
            else LOG_LEVEL_WARNING
        load_logging_handlers(
            [
                "sqlalchemy.engine.Engine",
            ],
            level=log_level,
        )


def new_app(configuration: dict = app_config):
    app = App(configuration)
    return app

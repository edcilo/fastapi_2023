from app.config import configuration as app_config
from app.core.config import config
from app.core.logging import LOG_LEVEL_INFO, LOG_LEVEL_WARNING, load_logging_handlers


def new_app(configuration: dict = app_config):
    config.load(configuration)

    log_level = LOG_LEVEL_INFO if config.app.environment == "development" else LOG_LEVEL_WARNING
    load_logging_handlers(
        [
            "sqlalchemy.engine.Engine",
        ],
        level=log_level,
    )

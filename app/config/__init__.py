from app.config.base import Config
from app.config.config import configuration as config_data


config = Config()
config.load(config_data)

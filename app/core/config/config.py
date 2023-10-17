from .appconfig import AppConfig
from .dbconfig import DBConfig


class Config:
    _instance = None

    app: AppConfig
    db: DBConfig

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def load(self, config: dict) -> None:
        self.app = AppConfig(**config["app"])
        self.db = DBConfig(**config["db"])

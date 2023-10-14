class DBConfig:
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password


class Config:
    _instance = None

    db: DBConfig

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def load(self, config: dict):
        self.db = DBConfig(**config["db"])

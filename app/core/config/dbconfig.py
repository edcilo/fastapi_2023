class DBConfig:
    def __init__(self,
                 engine: str,
                 host: str,
                 port: str,
                 dbname: str,
                 user: str,
                 password) -> None:
        self.engine = engine
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.url = self.get_url()

    def get_url(self):
        if self.engine == "postgres":
            return self.get_postgres_url()

    def get_postgres_url(self):
        return "postgresql+asyncpg://%s:%s@%s:%s/%s" % (
            self.user,
            self.password,
            self.host,
            self.port,
            self.dbname,
        )

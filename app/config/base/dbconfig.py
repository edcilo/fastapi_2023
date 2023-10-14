class DBConfig:
    def __init__(self, engine, host, port, dbname, user, password):
        self.engine = engine
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.url = self.get_url()

    def get_url(self):
        if self.engine == "postgresql":
            return self.get_postgresql_url()

    def get_postgresql_url(self):
        return "postgresql+asyncpg://%s:%s@%s:%s/%s" % (
            self.user,
            self.password,
            self.host,
            self.port,
            self.dbname,
        )

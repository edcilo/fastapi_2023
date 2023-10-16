class AppConfig:
    def __init__(self, name: str, version: str, environment: str) -> None:
        self.name = name
        self.version = version
        self.environment = environment

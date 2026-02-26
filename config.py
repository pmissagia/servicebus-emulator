import os


class Settings:
    def __init__(self):
        self.service_bus_connection_string = os.getenv(
            "SERVICE_BUS_CONNECTION_STRING",
            ""
        )

settings = Settings()

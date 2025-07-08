import os


class Config:
    api_key = os.environ.get("API_KEY")


CONFIG = Config()

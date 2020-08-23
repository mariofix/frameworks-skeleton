from dataclasses import dataclass
import os


@dataclass
class Config:
    SECRET_KEY: str = b"\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G.)\xaf"
    SERVER_NAME: str = "localhost:9000"
    SESSION_COOKIE_NAME: str = "cthulhu"
    EXPLAIN_TEMPLATE_LOADING: bool = True
    BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
    REGISTER_CORE = True

    @staticmethod
    def init_app(app):
        pass


@dataclass
class DevConfig(Config):
    URL: str = f"https://dev.mariofix.com"
    SESSION_COOKIE_SECURE: bool = False
    REMEMBER_COOKIE_SECURE = False
    DATABASE: str = "sqlite:///cthulhu.db"


@dataclass
class TestConfig(Config):
    URL: str = f"https://dev.mariofix.com"
    SESSION_COOKIE_SECURE: bool = False
    REMEMBER_COOKIE_SECURE = False
    DATABASE: str = ""


@dataclass
class ProdConfig(Config):
    URL: str = f"https://mariofix.com"
    SESSION_COOKIE_SECURE: bool = True
    REMEMBER_COOKIE_SECURE = True
    DATABASE: str = ""


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig
}

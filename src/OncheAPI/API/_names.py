from enum import Enum
from os.path import abspath, join, dirname

ROOT = dirname(__file__)
RENDER = f"{ROOT}/render/"


class AppRoute(Enum):
    HOMEPAGE = ("/", "index.html")
    DATABASE = ("/database/", "database.html")
    SETTINGS = ("/settings/", "settings.html")
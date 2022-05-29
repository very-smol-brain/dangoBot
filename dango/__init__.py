from .cogs import *
from .managers import *
from .config import *
from .setup import *

import sys
import datetime

def version():
    return "0.0.0.1"

def time():
    return datetime.datetime.now()

def config_version():
    return "0.1"

def path():
    return sys.path
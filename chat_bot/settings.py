import os
from distutils.util import strtobool

DEBUG = bool(strtobool(os.getenv('DEBUG', False)))

class Config:
    PROXY = os.getenv('PROXY', 'socks5h://78.46.200.216:31847')
    BOT_TOKEN = os.getenv('BOT_TOKEN', '1205108650:AAFLE6D3iQDuP3IneF7fwsMMm4jxCgm0ts0')

    DB_URI = os.getenv('DB_URI', 'sqlite:///:memory:')

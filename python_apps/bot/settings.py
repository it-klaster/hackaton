import os
from dotenv import load_dotenv
load_dotenv()


DEBUG = bool(os.getenv('DEBUG', False))
print(DEBUG)

class Config:
    PROXY = os.getenv('PROXY', 'socks5h://78.46.200.216:31847')
    BOT_TOKEN = os.getenv('BOT_TOKEN', '1205108650:AAFLE6D3iQDuP3IneF7fwsMMm4jxCgm0ts0')


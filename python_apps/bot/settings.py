import os

class Config:
    PROXY = os.getenv('PROXY', 'socks5h://54.39.16.26:35385')
    BOT_TOKEN = os.getenv('BOT_TOKEN', '1205108650:AAFLE6D3iQDuP3IneF7fwsMMm4jxCgm0ts0')

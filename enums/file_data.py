from enum import Enum
import os
import sys

class ConfigFiles(Enum):
    DB_CONFIG = '{}/etc/db_config.json'.format(sys.path[0])
    DISCORD_CONFIG = '{}/etc/discord.json'.format(sys.path[0])
    def __str__(self):
        return f'{self.value}'

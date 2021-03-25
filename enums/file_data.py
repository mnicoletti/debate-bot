from enum import Enum

class ConfigFiles(Enum):
    DB_CONFIG = '{}/etc/db_config.json'.format(os.path.dirname(os.path.realpath(__file__)))
    DISCORD_CONFIG = '{}/etc/discord.json'.format(os.path.dirname(os.path.realpath(__file__)))
    def __str__(self):
        return f'{self.value}'

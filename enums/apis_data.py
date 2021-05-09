from enum import Enum
import random

class APISData(Enum):
    MAP_JSON_URL = "https://fn.alphaleagues.com/v1/apex/map/?next="
    TRACKERGG_URL = "https://public-api.tracker.gg/v2/apex/standard"
    APEXSTATUS_URL = "https://api.mozambiquehe.re"
    def __str__(self):
        return f'{self.value}'

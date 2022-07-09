from enum import Enum

class APISData(Enum):
    TRACKERGG_URL = "https://public-api.tracker.gg/v2/apex/standard"
    APEXSTATUS_URL = "https://api.mozambiquehe.re"
    MAP_JSON_URI = "maprotation?version=2&auth={0}"
    PLAYER_STATUS_URI = "profile/origin/{0}?TRN-Api-Key={1}"
    PLAYER_RANK_URI = "bridge?version=5&platform=PC&player={0}&auth={1}"
    def __str__(self):
        return f'{self.value}'

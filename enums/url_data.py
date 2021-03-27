from enum import Enum
import random

class URLData(Enum):
    SEASON = "08"
    BASE_URL = "http://debatebot.freecluster.eu/apexdata"
    MAP_JSON_URL = "https://fn.alphaleagues.com/v1/apex/map/?next="
    IMG_MAP_BASE = "{0}/Maps/Season{1}".format(BASE_URL, SEASON)
    PREDATOR_LOGO = "{0}/GameIcons/apexpredator.jpeg".format(BASE_URL)
    TOTO_LOGO = "{0}/BotIcons/TotoLogo.png".format(BASE_URL)
    IMG_KINGSCANYON = "{0}/KingsCanyon".format(IMG_MAP_BASE)
    IMG_WORLDSEDGE = "{0}/WorldsEdge".format(IMG_MAP_BASE)
    IMG_OLYMPUS = "{0}/Olympus".format(IMG_MAP_BASE)
    def __str__(self):
        return f'{self.value}'

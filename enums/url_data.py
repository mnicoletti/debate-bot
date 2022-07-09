from enum import Enum

class URLData(Enum):
    SEASON = "09"
    BASE_URL = "https://max.nicoletti.co/debatebot"
    IMG_MAP_BASE = "{0}/Maps/Season{1}".format(BASE_URL, SEASON)
    PREDATOR_LOGO = "{0}/GameIcons/apexpredator.jpeg".format(BASE_URL)
    TOTO_LOGO = "{0}/BotIcons/TotoLogo.png".format(BASE_URL)
    IMG_KINGSCANYON = "{0}/KingsCanyon".format(IMG_MAP_BASE)
    IMG_WORLDSEDGE = "{0}/WorldsEdge".format(IMG_MAP_BASE)
    IMG_OLYMPUS = "{0}/Olympus".format(IMG_MAP_BASE)
    IMG_ARENAS = "{0}/Arenas".format(IMG_MAP_BASE)
    def __str__(self):
        return f'{self.value}'

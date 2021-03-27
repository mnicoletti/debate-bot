import logging
import json
import pycurl
from classes import database_mgmt
from enums import url_data
from io import BytesIO
import dateutil.parser

log = logging.getLogger(__name__)

class ApexMaps():
    def __init__(self):
        try:
            self.__map_url = url_data.URLData.MAP_JSON_URL
        except Exception as err:
            sys.exit(1)
        

    def obtain_map_rotation(self, next_amount=1):
        map_url = "{0}{1}".format(self.__map_url, next_amount)
        map_headers = ['Content-Type: application/json', 'User-Agent: Debate Discord Bot']
        map_io = BytesIO()
        map_next = []
        map_current = {}

        try:
            map_curl = pycurl.Curl()
            map_curl.setopt(map_curl.URL, map_url)
            map_curl.setopt(map_curl.HTTPHEADER, map_headers)
            map_curl.setopt(map_curl.WRITEDATA, map_io)
            map_curl.perform()
            map_curl.close()

            map_response = map_io.getvalue()

            json_response = json.loads(map_response)

            map_current = dict(
                map=json_response["map"], 
                remaining=int(json_response["times"]["remaining"]["minutes"])
                )

            for next_one in json_response["next"]:
                map_next.append(
                    dict(
                        map=next_one["map"],
                        duration=next_one["duration"],
                        start=dateutil.parser.isoparse(next_one["start"])
                    )
                )
            
            return (map_current, map_next)
        except Exception as err:
            logging.critical("Unexpected error ocurred: {}".format(err))
            return None
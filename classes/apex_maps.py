import logging
import json
import pycurl
from classes import database_mgmt
from io import BytesIO
import dateutil.parser

log = logging.getLogger(__name__)

class ApexMaps():
    def __init__(self, json_config_file):
        try:
            self.__apex_db = database_mgmt.DatabaseManager(json_config_file)
        except Exception as err:
            sys.exit(1)
        
        self.__map_url = ""
        self.__map_uri_path = ""

    def __renew_url_values(self):
        str_fields = ["map_url","map_uri_path"]
        str_table = "apex_data_config"

        try:
            dict_result = self.__apex_db.select_fields(str_fields, str_table)
            self.__map_url, self.__map_uri_path = dict_result[0]["map_url"], dict_result[0]["map_uri_path"]
        except Exception as err:
            logging.critical("Unexpected error ocurred: {}".format(err))


    def obtain_map_rotation(next_amount=1):
        map_url = "{0}{1}".format(self.__map_url, __self.__map_uri_path.format(next_amount))
        map_headers = ['Content-Type: application/json', 'User-Agent: Debate Discord Bot']
        map_io = BytesIO()
        map_next = []
        map_current = {}

        try:
            map_curl = pycurl.Curl()
            map_curl.set_opt(map_curl.URL, map_url)
            map_curl.set_opt(HTTPHEADER, map_headers)
            map_curl.set_opt(map_curl.WRITEDATA, map_io)
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
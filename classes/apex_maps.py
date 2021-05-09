import logging
import json
import pycurl
from classes import database_mgmt
from enums import url_data, file_data
from io import BytesIO
import dateutil.parser

log = logging.getLogger(__name__)

class ApexMaps():
    def __init__(self):
        try:
            self.__map_url = apis_data.APISData.MAP_JSON_URL
            self.__apex_db = database_mgmt.DatabaseManager(str(file_data.ConfigFiles.DB_CONFIG))
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

    def obtain_pois_from_current(self, current_map):
        str_fields = ["apex_pois.name"]
        str_tables = ["apex_pois", "apex_maps"]

        lst_where_fields = [dict(Name="apex_maps.name", Value=current_map), dict(Name="apex_pois.enabled",Value=1)]
        lst_relation_fields = [dict(Name="apex_maps.id", Value="apex_pois.id_maps")]
        
        try:
            cmd_output = self.__apex_db.select_fields(str_fields, str_tables, lst_where_fields, lst_relation_fields)
            return [ x['name'] for x in cmd_output ]
        except KeyError as err:
            log.critical("No key present at Apex Map POIS retrieval: {}".format(err))
        except Exception as err:
            log.critical("Unexpected error ocurred when retrieving Apex Map POIS for map {0}: {1}".format(current_map, err))
            
            return None
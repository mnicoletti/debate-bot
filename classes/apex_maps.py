import logging
import requests
import sys
from classes import database_mgmt, apis_mgmt
from enums import file_data, apis_data
from datetime import datetime

log = logging.getLogger(__name__)

class ApexMaps():
    def __init__(self):
        try:
            self.__api_mgmt = apis_mgmt.APISManager(str(file_data.ConfigFiles.API_CONFIG))
            self.__map_url = str(apis_data.APISData.APEXSTATUS_URL)
            self.__map_endpoint = str(apis_data.APISData.MAP_JSON_URI)
            self.__apex_db = database_mgmt.DatabaseManager(str(file_data.ConfigFiles.DB_CONFIG))
        except Exception as err:
            sys.exit(1)
        

    def obtain_map_rotation(self, type="battle_royale"):
        map_endpoint = self.__map_endpoint.format(self.__api_mgmt.apexstatus_token())
        map_url = "{0}/{1}".format(self.__map_url, map_endpoint)

        try:
            json_response = requests.get(map_url).json()

            map_current = dict(
                map=json_response[type]["current"]["map"], 
                remaining=int(json_response[type]["current"]["remainingMins"])
                )

            map_next = dict(
                        map=json_response[type]["next"]["map"],
                        duration=json_response[type]["next"]["DurationInMinutes"],
                        start=datetime.fromtimestamp(json_response[type]["current"]["end"])
                    )
            
            return (map_current, map_next)
        except Exception as err:
            logging.critical("Unexpected error occurred while obtaining rotation: {}".format(err))
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
            log.critical("Unexpected error occurred when retrieving Apex Map POIS for map {0}: {1}".format(current_map, err))
            
            return None
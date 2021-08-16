import logging
import json
import pycurl
import requests
from classes import database_mgmt, apis_mgmt
from enums import file_data
from io import BytesIO
import dateutil.parser

log = logging.getLogger(__name__)

class ApexStats():
    def __init__(self):
        try:
            self.__apexstatus_url = str(apis_data.APISData.APEXSTATUS_URL)
            self.__trackergg_url = str(apis_data.APISData.TRACKERGG_URL)
            self.__status_uri = str(apis_data.APISData.PLAYER_STATUS_URI)
            self.__ranked_uri = str(apis_data.APISData.PLAYER_RANK_URI)
            #self.__apex_db = database_mgmt.DatabaseManager(str(file_data.ConfigFiles.DB_CONFIG))
            self.__api_mgmt = apis_mgmt.APISManager(str(file_data.ConfigFiles.API_CONFIG))
        except Exception as err:
            sys.exit(1)
    
    def __obtain_player_stats(self, origin_id):
        player_status_endpoint = self.__status_uri.format(origin_id, self.__api_mgmt.trackergg_token())
        player_status_url = "{0}/{1}".format(self.__trackergg_url, player_status_endpoint)
        player_status_headers = ["Accept=application/json", "Accept-Encoding=gzip", 'User-Agent: Debate Discord Bot']
        status_io = BytesIO()

        try:
            status_curl = pycurl.Curl()
            status_curl.setopt(status_curl.URL, player_status_url)
            status_curl.setopt(status_curl.HTTPHEADER, player_status_headers)
            status_curl.setopt(status_curl.WRITEDATA, status_io)
            status_curl.perform()
            status_curl.close()

            status_response = status_io.getvalue()

            json_response = json.loads(status_response)

            return json_response
        except Exception as err:
            logging.critical("Unexpected error occured while obtaining player status: {}".format(err))
            return None
    
    def __obtain_player_rank(self, origin_id):
        player_status_endpoint = self.__ranked_uri.format(origin_id, self.__api_mgmt.apexstatus_token())
        player_status_url = "{0}/{1}".format(self.__apexstatus_url, player_status_endpoint)
        player_status_headers = ["Accept=application/json", "Accept-Encoding=gzip", 'User-Agent: Debate Discord Bot']

        try:
            json_response = requests.get(player_status_url, player_status_headers)

            return json_response
        except Exception as err:
            logging.critical("Unexpected error occured while obtaining player rank: {}".format(err))
            return None

    def obtain_player_stats(self, origin_id):
        raw_status = self.__obtain_player_stats(origin_id)
        raw_ranked = self.__obtain_player_rank(origin_id)
        player_status = {}

        if None in raw_status:
            return None
        
        for raw_response in raw_status['data']['segments']:
            if "overview" in raw_response['type']:
                player_status = dict(
                    life_level=int(raw_response['stats']['level']['value']),
                    life_kills=int(raw_response['stats']['kills']['value']),
                    life_dmg=int(raw_response['stats']['damage']['value']),
                    life_top=int(raw_response['stats']['timesPlacedtop3']['value'])
                )
        
        if None not in raw_ranked:
            player_ranked = dict(
                rank_score=int(raw_ranked['global']['rank']['rankScore']),
                rank_name=str(raw_ranked['global']['rank']['rankName']),
                rank_div=int(raw_ranked['global']['rank']['rankDiv']),
                rank_img=str(raw_ranked['global']['rank']['rankImg'])
            )
            player_status.update(player_ranked)

        return player_status
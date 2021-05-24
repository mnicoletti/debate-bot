import json
import logging

log = logging.getLogger(__name__)

class APISManager():
    def __init__(self, json_config_file):
        try:
            with open(json_config_file) as config_file:
                config = json.load(config_file)
        except IOError as er:
            log.critical("I/O Error({0}): {1} {2}".format(er.errno, er.strerror, json_config_file))
        except FileNotFoundError as er:
            log.critical("File not found: {}".format(er))
        except Exception as er:
            log.critical("Unexpected error: {}".format(er))
        
        try:
            self.__apexstatus_token = config["apexstatus_token"]
            self.__trackergg_token = config["trackergg_token"]
        except KeyError as err:
            log.critical("JSON file key not present setting up API Tokens: {}".format(err))
        except Exception as err:
            log.critical("Unexpected error ocurred while setting up API Tokens: {}".format(err))
    
    def apexstatus_token(self):
        return self.__apexstatus_token
    
    def trackergg_token(self):
        return self.__trackergg_token
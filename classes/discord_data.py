import json
import logging

log = logging.getLogger(__name__)

class DiscordBotJsonData():
    def __init__(self, json_config_file):
        try:
            with open(json_config_file) as config_file:
                config = json.load(config_file)
        except IOError as er:
            log.critical("I/O Error({0}): {1}".format(er.errno, er.strerror))
        except FileNotFoundError as er:
            log.critical("File not found: {}".format(er))
        except Exception as er:
            log.critical("Unexpected error: {}".format(er))
        self.__token = config["token"]
        self.__guild_name = config["guild"]
        self.__log_path = config["log_path"]
        self.__log_file = config["log_file"]
    
    def token(self):
        return self.__token
    
    def guild_name(self):
        return self.__guild_name
    
    def log_path(self):
        return self.__log_path
    
    def log_file(self):
        return self.__log_file
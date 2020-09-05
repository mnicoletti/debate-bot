import json

class DiscordJsonData():
    def __init__(self, json_config_file):
        with open(json_config_file) as config_file:
            config = json.load(config_file)
        self.__token = config["token"]
        self.__guild_name = config["guild"]
    
    def token(self):
        return self.__token
    
    def guild_name(self):
        return self.__guild_name
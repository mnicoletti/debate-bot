import json
from datetime import datetime
import logging

log = logging.getLogger(__name__)

class PerfectData:
    def __init__(self, json_config_file):
        self.__config_file = json_config_file
        try:
            with open(self.__config_file) as config_file:
                config = json.load(config_file)
        except IOError as er:
            log.critical("I/O Error({0}): {1}".format(er.errno, er.strerror))
        except FileNotFoundError as er:
            log.critical("File not found: {}".format(er))
        except Exception as er:
            log.critical("Unexpected error: {}".format(er))
        try:
            self.__id = config["id"]
            self.__nickname = config["nickname"]
            self.__full_id = "%s#%s" % (self.__nickname, str(self.__id))
            self.__offline_date = datetime.strptime(config["offline_date"], "%x %X")
        except KeyError as err:
            log.critical("JSON file key not present: {}".format(err))
        except Exception as err:
            log.critical("Unexpected error ocurred: {}".format(err))
    
    def id(self):
        return self.__id

    def nickname(self):
        return self.__nickname
    
    def full_id(self):
        return self.__full_id
    
    def offline_date(self):
        return self.__offline_date
    
    def update_offline_date(self):
        date_now = datetime.now().strftime("%x %X")

        try:
            with open(self.__config_file, "r") as config_file:
                config = json.load(config_file)
        except IOError as er:
            log.critical("I/O Error({0}): {1}".format(er.errno, er.strerror))
        except FileNotFoundError as er:
            log.critical("File not found: {}".format(er))
        except Exception as er:
            log.critical("Unexpected error: {}".format(er))
        try:
            config["offline_date"] = date_now
        except KeyError as err:
            log.critical("JSON file key not present: {}".format(err))
        except Exception as err:
            log.critical("Unexpected error ocurred: {}".format(err))

        try:
            with open(self.__config_file, "w") as config_file:
                json.dump(config, config_file)
        except IOError as er:
            log.critical("I/O Error({0}): {1}".format(er.errno, er.strerror))
        except FileNotFoundError as er:
            log.critical("File not found: {}".format(er))
        except Exception as er:
            log.critical("Unexpected error: {}".format(er))

        try:
            self.__offline_date = datetime.strptime(config["offline_date"], "%x %X")
        except KeyError as err:
            log.critical("JSON file key not present: {}".format(err))
        except Exception as err:
            log.critical("Unexpected error ocurred: {}".format(err))
        log.info("Perfect se puso offline.")
        return True
    
    def calculate_last_offline(self) -> str:
        date_now = datetime.now()
        date_then = self.__offline_date
        date_delta = date_now - date_then
        date_delta_seconds = date_delta.total_seconds()
        days, seconds = divmod(date_delta_seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        if days > 0:
            return "%d dias, %d horas, %d minutos, %d segundos" % (days, hours, minutes, seconds)
        elif hours > 0:
            return "%d horas, %d minutos, %d segundos" % (hours, minutes, seconds)
        elif minutes > 0:
            return "%d minutos, %d segundos" % (minutes, seconds)
        elif seconds > 0:
            return "%d segundos" % seconds
        else:
            return "online"

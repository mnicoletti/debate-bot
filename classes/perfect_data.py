import json
from datetime import datetime
import logging
from classes import database_mgmt

log = logging.getLogger(__name__)

class PerfectData:
    def __init__(self, json_config_file):
        self.__config_file = json_config_file
        try:
            self.__perfect_db = database_mgmt.DatabaseManager(json_config_file)
        except Exception as er:
            log.critical("Unexpected error: {}".format(er))
        
        self.__renew_perfect_values()
    
    def __renew_perfect_values(self):
        str_fields = ["id", "nickname", "offline_date"]
        str_table = "perfect_offline"

        try:
            dict_result = self.__perfect_db.select_fields(str_fields, str_table)
            self.__id = dict_result[0]["id"]
            self.__nickname = dict_result[0]["nickname"]
            self.__full_id = "{0}#{1}".format(self.__nickname, self.__id)
            self.__offline_date = dict_result[0]["offline_date"]
        except KeyError as err:
            log.critical("Response key not present: {}".format(err))
        except Exception as err:
            log.critical("Unexpected error ocurred while renewing values: {}".format(err))

    def __renew_offline_date(self):
        str_fields = ["offline_date"]
        str_table = "perfect_offline"

        try:
            dict_result = self.__perfect_db.select_fields(str_fields, str_table)
            self.__offline_date = datetime.strptime(dict_result[0]["offline_date"], "%x %X")
        except KeyError as err:
            log.critical("Response key not present: {}".format(err))
        except Exception as err:
            log.critical("Unexpected error ocurred while renewing offline dates: {}".format(err))

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
        str_table = "perfect_offline"
        lst_update_fields = [dict(Name="offline_date",Value=date_now)]
        lst_where_fields = [dict(Name="id", Value=self.__id)]

        try:
            self.__perfect_db.update_fields(lst_update_fields, lst_where_fields, table)
            self.__renew_offline_date()
        except KeyError as err:
            log.critical("JSON file key not present: {}".format(err))
            return True
        except Exception as err:
            log.critical("Unexpected error ocurred: {}".format(err))
            return False
            
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

    def retrieve_perfect_message(self, msg_type) -> [str]:
        str_fields = ["string_frases.mensaje"]
        str_tables = ["string_frases", "funciones_frases"]
        lst_where_fields = [dict(Name="funciones_frases.funcion", Value=msg_type)]
        lst_relation_fields = [dict(Name="string_frases.id_funcion", Value="funciones_frases.id")]
        try:
            cmd_output = self.__perfect_db.select_fields(str_fields, str_tables, lst_where_fields, lst_relation_fields)

            return [ x['mensaje'] for x in cmd_output ]
        except KeyError as err:
            log.critical("No key present at message retrieval: {}".format(err))
        except Exception as err:
            log.critical("Unexpected error occurred while retrieving Perfect messages: {}".format(err))
        
        return False
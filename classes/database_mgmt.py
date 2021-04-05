import json
import logging
import mariadb

log = logging.getLogger(__name__)

class DatabaseManager():
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
        
        try:
            self.__mysql_conf = {
                "host": "",
                "port": 3306,
                "user": "",
                "pass": "",
                "db_name": ""
            }

            self.__mysql_conf["host"] = config["host"]
            self.__mysql_conf["port"] = config["port"]
            self.__mysql_conf["user"] = config["user"]
            self.__mysql_conf["pass"] = config["pass"]
            self.__mysql_conf["db_name"] = config["db_name"]
        except KeyError as err:
            log.critical("JSON file key not present: {}".format(err))
        except Exception as err:
            log.critical("Unexpected error ocurred: {}".format(err))
    
    def __connect(self):
        try:
            self.__db_conn = mariadb.connect(
                user = self.__mysql_conf["user"],
                password = self.__mysql_conf["pass"],
                host = self.__mysql_conf["host"],
                port = self.__mysql_conf["port"],
                database = self.__mysql_conf["db_name"],
                autocommit = True
            )
        except mariadb.Error as err:
            logging.critical("Unable to connect to MariaDB : {}".format(err))
        except Exception as err:
            logging.critical("Unexpected error ocurred while connecting to MariaDB: {}".format(err))
    
    def __close(self):
        try:
            self.__db_conn.close()
        except mariadb.Error as err:
            logging.critical("Unable to close connection with MariaDB: {}".format(err))
        except Exception as err:
            logging.critical("Unexpected error occured while closing MariaDB connection: {}".format(err))

    def __map_select_fields(self, map_fields):
        return ", ".join(map_fields)

    def __map_update_fields(self, map_fields):
        mapper = ", ".join(["{0}=\"{1}\"".format(x["Name"], x["Value"]) for x in map_fields])

    def __map_where(self, map_where_fields, conditional):
        mapper = ["{0}=\"{1}\"".format(x["Name"], x["Value"]) for x in map_where_fields]

        return " {0} ".format(conditional).join(mapper)
        
    def select_fields(self, map_field, table, map_where=None, condition="AND"):
        select_command = "SELECT {0} FROM {1}"

        str_fields = self.__map_select_fields(map_field)
        
        if not isinstance(table, str):
            table = ", ".join(table)

        if map_where != None:
            where_fields = self.__map_where(map_where, condition)
            full_command = "{0} WHERE {1}".format(select_command.format(str_fields, table), where_fields)
        else:
            full_command = select_command.format(str_fields, table)

        lst_response = []

        try:
            self.__connect()
            self.__cursor = self.__db_conn.cursor(dictionary=True)
            self.__cursor.execute(full_command)
            
            lst_response = [ x for x in self.__cursor ]
            
            self.__close()

            return lst_response
        except mariadb.Error as err:
            logging.critical("Error ocurred when selecting from database: {}".format(err))
        except Exception as err:
            logging.critical("Unexpected error ocurred while executing SELECT command: {}".format(err))
            return False

    def select_fields_related_conditional(self, map_field, map_where, map_relations, tables):
        return

    def update_fields(self, map_field, map_where, table, condition="AND"):
        update_command = "UPDATE {0} SET {1}=%s WHERE {2}=%s;"

        update_field_name = map_field[0]["Name"]
        where_field_name = map_where[0]["Name"]

        try:
            self.__connect()
            self.__cursor = self.__db_conn.cursor()
            self.__cursor.execute(update_command.format(table, update_field_name, where_field_name),(map_field[0]["Value"],map_where[0]["Value"]))
            self.__close()
        except mariadb.Error as err:
            logging.critical("Error ocurred when updating database: {}".format(err))
        except Exception as err:
            logging.critical("Unexpected error ocurred while executing UPDATE command: {}".format(err))
            return False
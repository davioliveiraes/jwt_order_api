import sqlite3
from sqlite3 import Connection

class __DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__conn = None
    
    def connect(self) -> None:
        self.__conn = sqlite3.connect(self.__connection_string)
    
    def get_connection(self) -> Connection:
        if self.__conn is None:
            self.connect()
        return self.__conn
    
db_connection_handler = __DBConnectionHandler()    

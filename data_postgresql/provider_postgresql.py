from data.provider_db import ProviderDb
from data_postgresql.postgresql_connection_string_builder import PostgreSQLConnectionStringBuilder
import psycopg2


class ProviderPostgreSQL(ProviderDb):

    connection = None
    cursor = None

    __connection_string_builder = None

    def __init__(self, connection_string):
        ProviderDb.__init__(self, connection_string)

    def _initialize(self):
        self.__connection_string_builder = PostgreSQLConnectionStringBuilder(
            self.connection_string)

    def _on_open_connection(self):
        self.connection = psycopg2.connect(
            host=self.__connection_string_builder.get_host(),
            port=self.__connection_string_builder.get_port(),
            dbname=self.__connection_string_builder.get_database(),
            user=self.__connection_string_builder.get_username(),
            password=self.__connection_string_builder.get_password())

        self.cursor = self.connection.cursor()

    def _on_close_connection(self):
        self.cursor.close()
        self.connection.close()

    def _on_commit_transaction(self):
        self.connection.commit()

    def _on_execute(self, cmd, args):
        self.cursor.execute(cmd, args)
        return self.cursor

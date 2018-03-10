from data.connection_string_builder import ConnectionStringBuilder


class PostgreSQLConnectionStringBuilder(ConnectionStringBuilder):
    def __init__(self, connectionString):
        ConnectionStringBuilder.__init__(self, connectionString)

    def get_host(self):
        return self.get_item("host")

    def get_port(self):
        return self.get_item("port")

    def get_database(self):
        return self.get_item("database")

    def get_database(self):
        return self.get_item("database")

    def get_username(self):
        return self.get_item("username")

    def get_password(self):
        return self.get_item("password")

    def set_host(self, value):
        return self.set_item("host", value)

    def set_port(self, value):
        return self.get_item("port", value)

    def set_database(self, value):
        return self.get_item("database", value)

    def set_database(self, value):
        return self.get_item("database", value)

    def set_username(self, value):
        return self.get_item("username", value)

    def set_password(self, value):
        return self.get_item("password", value)
class ConnectionStringBuilder:

    connection_string = ""

    def __init__(self, connectionString):
        self.__install_cntstring(connectionString)

    def get_item(self, key):
        key = key.lower()
        for k in self.items:
            if k.lower() == key:
                return self.items[k]

    def set_item(self, key, value):
        self.items[key] = value
        self.__refresh_cntstring()

    def __refresh_cntstring(self):
        cntString = ""
        index = 0

        for k in self.items:
            if index > 0:
                cntString += ";"
            cntString += "{}={}".format(k, self.items[k])
            index += 1

        self.connection_string = cntString

    def __install_cntstring(self, connectionString):
        self.connection_string = connectionString
        self.items = {}
        parts = connectionString.split(";")

        for p in parts:
            if p.strip() == "":
                continue

            values = p.split("=")
            if len(values) < 2:
                continue

            self.items[values[0]] = values[1]

import threading


class Provider:

    connection_string = ""
    sync_object = threading.Lock()

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self._initialize()

    def _initialize(self):
        pass

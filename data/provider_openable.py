import provider


class ProviderOpenable(provider.Provider):

    __cntOpen = 0

    def __init__(self, connection_string):
        provider.Provider.__init__(self, connection_string)

    def open_connection(self):
        try:
            self.sync_object.acquire()

            self.__cntOpen += 1
            if self.__cntOpen > 1:
                return

            self._on_open_connection()

        finally:
            self.sync_object.release()

    def _on_open_connection(self):
        pass

    def close_connection(self):
        try:
            self.sync_object.acquire()

            self.__cntOpen -= 1
            if self.__cntOpen > 0:
                return

            self._on_close_connection()

        finally:
            self.sync_object.release()

    def _on_close_connection(self):
        pass
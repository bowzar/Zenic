import provider_openable
import threading


class ProviderDb(provider_openable.ProviderOpenable):

    __cntTransaction = 0

    def __init__(self, connection_string):
        provider_openable.ProviderOpenable.__init__(self, connection_string)

    def begin_transaction(self):
        try:
            self.sync_object.acquire()

            self.__cntTransaction += 1
            if self.__cntTransaction > 1:
                return

            self._on_begin_transaction()

        finally:
            self.sync_object.release()

    def _on_begin_transaction(self):
        pass

    def commit_transaction(self):
        try:
            self.sync_object.acquire()

            self.__cntTransaction -= 1
            if self.__cntTransaction > 0:
                return

            self._on_commit_transaction()

        finally:
            self.sync_object.release()

    def _on_commit_transaction(self):
        pass

    def rollback_transaction(self):
        try:
            self.sync_object.acquire()

            self.__cntTransaction -= 1
            if self.__cntTransaction > 0:
                return

            self._on_rollback_transaction()

        finally:
            self.sync_object.release()

    def _on_rollback_transaction(self):
        pass

    def execute(self, cmd, args, callback=None):

        try:
            self.sync_object.acquire()

            result = self._on_execute(cmd, args)
            if callable != None:
                return callback(result)

            return result

        finally:
            self.sync_object.release()

    def _on_execute(self, cmd, args):
        pass
from utils.connection import Connection

class Litesqlite:
    @staticmethod
    def connect(db_name: str = None, check_same_thread: bool = False, timeout: int = 0):
        return Connection(db_name=db_name, check_same_thread=check_same_thread, timeout=timeout)


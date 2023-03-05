import sqlite3

import utils.table
from utils import table


class Connection:
    def __init__(self, db_name=None, check_same_thread: bool = False, timeout: int = 0):
        self.__db_name = db_name
        self.__check_same_thread = check_same_thread
        self.__timeout = timeout

    def run_sql(self, sql):
        conn = sqlite3.connect(database=self.__db_name, timeout=self.__timeout,
                               check_same_thread=self.__check_same_thread)
        cursor = conn.cursor()
        r = cursor.execute(sql)
        conn.commit()
        return r

    def create_table(self, name, structure):
        req = f"CREATE TABLE IF NOT EXISTS \"{name}\" ("
        last = list(structure)[-1]
        for i in structure:
            req += f"'{i}' {structure[i]}"
            if i != last:
                req += ", "
        req += ")"
        self.run_sql(req)
        return table.Table(table=name, db_name=self.__db_name, check_same_thread=self.__check_same_thread,
                           timeout=self.__timeout)

    def drop_table(self, database_table: utils.table.Table):
        name = database_table.get_name()
        self.run_sql(f"DROP TABLE {name}")

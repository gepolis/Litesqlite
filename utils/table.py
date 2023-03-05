import sqlite3


class Table:
    def __init__(self, table: str, db_name: str = None, check_same_thread: bool = False, timeout: int = 0):
        self.__db_name = db_name
        self.__table = table
        self.__check_same_thread = check_same_thread
        self.__timeout = timeout

    @staticmethod
    def __type_man(i):
        if type(i) == str:
            return f"'{i}'"
        else:
            return i

    def get_name(self):
        return self.__table

    def run_sql(self, sql):
        conn = sqlite3.connect(database=self.__db_name, timeout=self.__timeout,
                               check_same_thread=self.__check_same_thread)
        cursor = conn.cursor()
        r = cursor.execute(sql)
        conn.commit()
        return r

    def select(self, filters=None, order_by: str = None, order_type: str = "ASC"):  # , columns: dict = None, ):
        req = f"SELECT "
        # if columns is None:
        req += f"* FROM {self.__table} "
        # else:
        #    last = list(columns)[-1]
        #    for i in columns:
        #        req += i
        #        if i != last:
        #            req += ", "
        #    req += f" FROM {self.__table} "
        if filters is not None:
            req += f"WHERE {filters}"
        if order_by is not None:
            req += f"ORDER BY '{order_by}' {order_type}"
        return self.run_sql(req)

    def insert(self, data):
        # INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
        req = f"INSERT INTO {self.__table} ("
        last = list(data)[-1]
        for i in data:
            req += i
            if i != last:
                req += ", "
        req += ") VALUES ("
        for i in data:
            req += f"{self.__type_man(data[i])}"
            if i != last:
                req += ", "
        req += ")"
        self.run_sql(req)

    def update(self, set_values, where=None):
        # INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
        req = f"UPDATE {self.__table} SET"
        last = list(set_values)[-1]
        for i in set_values:
            req += f" {i} = {set_values[i]}"
            if i != last:
                req += ", "
        if where is not None:
            req += f" WHERE {where}"
        self.run_sql(req)

    def delete(self, where=None):
        req = f"DELETE FROM {self.__table}"
        if where is not None:
            req += f" WHERE {where}"
        self.run_sql(req)

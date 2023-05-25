from os import environ
from typing import Final

import mysql.connector as conn
from aiogram.types import Message


class TOKEN:
    TOKEN: Final = environ.get('admin_1', 'define me!')


class DB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def result_fetch(self, needtodisconnect: bool, sql: str):
        command = ''
        try:
            dataBase = conn.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except conn.InternalError:
            print("Internal error occur")
        finally:
            if needtodisconnect:
                if dataBase.is_connected():
                    dataBase.close()
                    dataBase.cursor().close()
            if not needtodisconnect:
                try:
                    command = sql
                    cursor = dataBase.cursor(buffered=True)
                    cursor.execute(sql)
                    result_from_cursor = cursor.fetchall()
                finally:
                    if dataBase.is_connected():
                        dataBase.close()
                        cursor.close()
                        return result_from_cursor

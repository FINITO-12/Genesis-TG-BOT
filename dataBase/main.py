from os import environ
from typing import Final

import mysql.connector
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
            cursor = dataBase.cursor(buffered=True)
        except conn.InternalError:
            print("Internal error occur")
        finally:
            if needtodisconnect:
                if dataBase.is_connected():
                    dataBase.close()
                    cursor.close()
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

    def insert_users(self, needtodisconnect: bool, message: Message):
        attempts = 0
        user_id = message.chat.id
        try:
            dataBase = conn.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = dataBase.cursor(buffered=True)
            sql = "SELECT * FROM users WHERE user_id=(%s)"
            val = (user_id,)
            # u = val[0]
            cursor.execute(sql, val)
            res = cursor.fetchall()
            while attempts < 1:
                try:
                    shit = res[0]
                    (a1, a2, a3, a4, a5) = shit
                    if type(a2) == int:
                        print(str(user_id) + " ID | Account exists")
                        return a2
                except (IndexError):
                    print("Account does not exist")
                finally:
                    attempts = attempts + 1
                    self.tryRegistration(message=message)
        # except mysql.connector.Error as e:
        # print("Error reading")
        finally:
            if dataBase.is_connected():
                dataBase.close()
                cursor.close()
                print("MySQL Connection for @TryCheck is closed")

    def tryRegistration(self, message: Message):
        try:
            dataBase = conn.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = dataBase.cursor(buffered=True)
            sql = "INSERT IGNORE INTO users (user_id, role, name, admin) VALUES (%s,%s,%s,%s)"
            val = (message.chat.id, "user", message.from_user.first_name, 0,)
            cursor.execute(sql, val)
            dataBase.commit()
            print(str(cursor.rowcount) + " record(s) inserted")
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if dataBase.is_connected():
                dataBase.close()
                cursor.close()

    '''
                    await tryRegistration(message=message)
        except mysql.connector.Error as e:
            print("Error reading")
        finally:
            if dataBase.is_connected():
                dataBase.close()
                cursor.close()
                warning("MySQL Connection for @TryCheck is closed")

    async def tryRegistration(message: types.Message):
        global dataBase, cursor

        try:
            dataBase = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="telegram bot")
            cursor = dataBase.cursor(buffered=True)
            sql = "INSERT IGNORE INTO users (user_id, name) VALUES (%s,%s)"
            val = (message.from_user.id, message.from_user.first_name)
            cursor.execute(sql, val)
            dataBase.commit()
            info(str(cursor.rowcount) + " record inserted")

        except mysql.connector.Error as e:
            print("Error reading data from MySQL Table", e)
        finally:
            if dataBase.is_connected():
                dataBase.close()
                cursor.close()
                warning("MySQL Connection for @TryRegistration is closed")'''

import logging

import mysql.connector as conn
def RunDB(host="localhost", user="root", password=""):
    try:
        dataBase = conn.connect(
            host=host,
            user=user,
            password=password
        )

        if dataBase.is_connected():
            print("SHIT")
    except conn.InternalError:
        print("Shit happens")
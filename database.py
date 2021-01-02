import sqlite3

connect = sqlite3.connect("download_cache.db")
cursor = connect.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS downloaded (nameetc TEXT,dir TEXT, name TEXT)")
connect.commit()


def getData():
    cursor.execute("SELECT * FROM downloaded")
    datas = cursor.fetchall()
    return datas


def addData(name, dir, justname):
    cursor.execute(
        f"INSERT INTO downloaded VALUES ('{name}','{dir}', '{justname}')")
    connect.commit()


def delData(name, dir, justname):
    cursor.execute(
        f"DELETE FROM downloaded WHERE nameetc = '{name}' AND dir = '{dir}' AND name = '{justname}'")
    connect.commit()

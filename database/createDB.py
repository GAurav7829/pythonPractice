import pymysql

db = pymysql.connect(host="localhost", user="root", password="")

cursor = db.cursor()

sql = """
    CREATE DATABASE projectdb
"""

cursor.execute(sql)
print("DataBase Created...")

db.close()
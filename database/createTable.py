import pymysql

db = pymysql.connect(host="localhost", user="root", password="", db="projectdb")

cursor = db.cursor()

sql = """
    CREATE TABLE testTable(
        name CHAR(20) NOT NULL,
        location CHAR(100),
        gender CHAR(1),
        age INTEGER
    )
"""

cursor.execute(sql)
print("Table Created...")

db.close()
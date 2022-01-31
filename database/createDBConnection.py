import pymysql

db = pymysql.connect(host="localhost", user="root", password="", db="projectdb")

cursor = db.cursor()
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print(data)

db.close()
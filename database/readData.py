from pydoc import locate
from unittest import result
import pymysql

db = pymysql.connect(host="localhost", user="root", password="", db="projectdb")

cursor = db.cursor()

sql = """
    SELECT * FROM testTable
"""

try:
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        name = row[0]
        location = row[1]
        gender = row[2]
        age = row[3]
        print("Name: %s, Location: %s, Gender: %s, Age: %s" %(name, location, gender, age))

except:
    print('Error: Unable to fetch data...')

db.close()
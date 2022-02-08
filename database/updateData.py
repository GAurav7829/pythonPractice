from pydoc import locate
from unittest import result
import pymysql

db = pymysql.connect(host="localhost", user="root", password="", db="projectdb")

cursor = db.cursor()

sql = """
    UPDATE testTable SET age = 40 WHERE name = 'sonu'
"""

try:
    cursor.execute(sql)
    db.commit()
    print('Age update successfully...')
except:
    print('Error: Unable to update data...')
    db.rollback()

db.close()
from pydoc import locate
from unittest import result
import pymysql

db = pymysql.connect(host="localhost", user="root", password="", db="projectdb")

cursor = db.cursor()

sql = """
    DELETE FROM testTable WHERE name = 'sonu'
"""

try:
    cursor.execute(sql)
    db.commit()
    print('data deleted successfully...')
except:
    print('Error: Unable to delete data...')
    db.rollback()

db.close()
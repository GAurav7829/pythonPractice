import pymysql

db = pymysql.connect(host="localhost", user="root", password="", db="projectdb")

cursor = db.cursor()

sql = """
    INSERT INTO testTable(name, location, gender, age)
    VALUES('grv','delhi','M', 27);
"""

try:
    cursor.execute(sql)
    db.commit()
    print('Data Inserted Successfully...')
except:
    print('Error: Rollback...')
    db.rollback()

db.close()
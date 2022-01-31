import pymysql

db = pymysql.connect(host="localhost", user="root", password="", db="projectdb")

cursor = db.cursor()

mySql_insert_query = """
    INSERT INTO testTable(name, location, gender, age)
    VALUES(%s, %s, %s, %s);
"""
records_to_insert = [('monu','delhi','M',18),
                    ('sonu', 'delhi', 'M', 28),
                    ('savan', 'delhi', 'M', 20)]

try:
    cursor.executemany(mySql_insert_query,records_to_insert)
    db.commit()
    print('Data Inserted Successfully...')
except:
    db.rollback()
    print('Error: DB Rollback...')
finally:
    db.close()
    print('DB closed...')
import sqlite3

conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()


sql = '''update celebs set photo=replace(photo,'nphinity','software4rfid')'''
cursor.execute(sql)

# commit changes to db
conn.commit()
conn.close()

print("YO")
import sqlite3

conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

# create a table in db
sql1 = "create table celebs(celebID integer PRIMARY KEY, firstname text, lastname text, age integer, email text, \
photo text, bio text)"

sql2 = "create table members(memberID integer PRIMARY KEY, firstname text, lastname text, age integer, email text, \
bio text)"

sql3 = "create table creds(userID integer PRIMARY KEY, username text, password text)"

pop1 =  "insert into celebs values (?,?,?,?,?,?,?)"
data1 = ((1, "Angelina", "Jolie", 40, "angie@hollywood.us", "http://www.software4rfid.com/pics/aj.jpg",""),
         (2, "Brad", "Pitt", 51, "brad@hollywood.us", "http://www.software4rfid.com/pics/bp.jpg",""),
         (3, "Snow", "White", 21, "sw@disney.org", "http://www.software4rfid.com/pics/sw.jpg",""),
         (4, "Darth", "Vader", 29, "dv@darkside.me", "http://www.software4rfid.com/pics/dv.jpg",""),
         (5, "Taylor", "Swift", 25, "ts@1989.us", "http://www.software4rfid.com/pics/ts.jpg",""),
         (6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "http://www.software4rfid.com/pics/bk.jpg",""),
         (7, "Selena", "Gomez", 23, "selena@hollywood.us", "http://www.software4rfid.com/pics/sg.jpg",""),
         (8, "Stephen", "Curry", 27, "steph@golden.bb", "http://www.software4rfid.com/pics/sc.jpg",""))

pop2 = "insert into members values (?,?,?,?,?,?)"
data2 = ((1, "Kyle", "Linsday", 23, "linsdakr@dukes.jmu.edu", "I have red hairs on my head."),
         (2, "Chris", "Byron", 20, "byroncr@dukes.jmu.edu", "I was born in San Diego, CA and raised there until I was 3.  I then moved to Reston, VA which is Northern Viginia and have lived there ever since."))

pop3 = "insert into creds values (?,?,?)"
data3 = ((1, "kyle", "password"),
         (2, "chris", "password"))

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.executemany(pop1,data1)
cursor.executemany(pop2,data2)
cursor.executemany(pop3,data3)


# commit changes to db
conn.commit()
conn.close()

print("YO")
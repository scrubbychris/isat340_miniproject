import sqlite3

conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

gin = "kyle"




cursor.execute('''SELECT * FROM creds WHERE username="'''+gin+'''"''')
#print(('''SELECT * FROM creds WHERE username="'''+gin+'''"'''))

row = cursor.fetchone()

if row == None:
    error = 'User does not exist. Please try again.'
elif request.form['password'] != row[2]:
    error = 'Incorrect password.  Please try again.'
else:
    return redirect(url_for('info'))

# commit changes to db
conn.close()

print(row)
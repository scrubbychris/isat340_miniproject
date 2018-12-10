__author__ = 'Tony Teate'

#imports
import sqlite3
from flask import Flask, render_template
from flask import request, redirect, url_for

#instantiate
app = Flask(__name__)
# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    username = ''
    password = ''
    list = []

    if request.method == 'POST':
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM creds WHERE username="'''+ request.form['username']+'''"''')
        row = c.fetchone()
        conn.close()

        if row == None:
            error = 'User does not exist. Please try again.'
        elif request.form['password'] != row[2]:
            error = 'Incorrect password.  Please try again.'
        else:
            return redirect(url_for('info'+str(row[0])))
    return render_template('login.htm', error=error)

@app.route('/info1', methods=['GET', 'POST'])
def info1():
    memberID=None
    firstname = ''
    lastname = ''
    age = None
    email = ''
    bio = ''
    success = False
    profile = "1"

    # this is called when page is first loaded
    if request.method == 'GET':
        # connect to the database and select one record (row of data)
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members WHERE memberID="'''+profile+'''"''')
        row = c.fetchone()
        #print (row)
        #if the row contains data, store it in variables
        if row:
            memberID = row[0]
            firstname = row[1]
            lastname = row[2]
            age = row[3]
            email = row[4]
            bio = row[5]
        #close connection to the db
        conn.close()
        #print(row)
    #this is called when the button is clicked
    if request.method == 'POST':
        #get the data from the form and store it in variables
        #this uses the request method to get the data from named elements on the form
        memberID=request.form['memberID']
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        age =request.form['age']
        email =request.form['email']
        bio =request.form['bio']
        success = True
        # now store the data from the form into the db
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members WHERE memberID="'''+profile+'''"''')
        row = c.fetchone()
        if row: # if row exists, update the data in the row
            c.execute('''UPDATE members SET firstname = ?, lastname = ?, age = ?, email = ?, bio = ? WHERE memberID="'''+profile+'''"''',
                      (firstname, lastname, age, email, bio))
        else: # if row does not exist, insert data into the row
            c.execute('''INSERT INTO members VALUES (?, ?, ?, ?, ?, ?)''',
                      (memberID, firstname, lastname, age, email, bio))
        conn.commit()
        conn.close()
    return render_template('profile'+profile+'.htm', memberID=memberID, firstname=firstname, lastname=lastname, age=age, email=email, bio=bio, success=success)


@app.route('/info2', methods=['GET', 'POST'])
def info2():
    memberID=None
    firstname = ''
    lastname = ''
    age = None
    email = ''
    bio = ''
    success = False
    profile = "2"

    # this is called when page is first loaded
    if request.method == 'GET':
        # connect to the database and select one record (row of data)
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members WHERE memberID="'''+profile+'''"''')
        row = c.fetchone()
        #print (row)
        #if the row contains data, store it in variables
        if row:
            memberID = row[0]
            firstname = row[1]
            lastname = row[2]
            age = row[3]
            email = row[4]
            bio = row[5]
        #close connection to the db
        conn.close()
        #print(row)
    #this is called when the button is clicked
    if request.method == 'POST':
        #get the data from the form and store it in variables
        #this uses the request method to get the data from named elements on the form
        memberID=request.form['memberID']
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        age =request.form['age']
        email =request.form['email']
        bio =request.form['bio']
        success = True
        # now store the data from the form into the db
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members WHERE memberID="'''+profile+'''"''')
        row = c.fetchone()
        if row: # if row exists, update the data in the row
            c.execute('''UPDATE members SET firstname = ?, lastname = ?, age = ?, email = ?, bio = ? WHERE memberID="'''+profile+'''"''',
                      (firstname, lastname, age, email, bio))
        else: # if row does not exist, insert data into the row
            c.execute('''INSERT INTO members VALUES (?, ?, ?, ?, ?, ?)''',
                      (memberID, firstname, lastname, age, email, bio))
        conn.commit()
        conn.close()
    return render_template('profile'+profile+'.htm', memberID=memberID, firstname=firstname, lastname=lastname, age=age, email=email, bio=bio, success=success)



@app.route('/view_all_celebs')
def view_all():
    celebID=None
    firstname = ''
    lastname = ''
    age = ''
    email = ''
    photo = ''
    bio = ''

    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM celebs ORDER BY celebID''')
    rows = c.fetchall()
    conn.close()
    #return
    return render_template('view_all_celebs.htm', rows=rows)

@app.route('/view_one_celeb')
def view_one():
    celebID=None
    firstname = ''
    lastname = ''
    age = ''
    email = ''
    photo = ''
    bio = ''

    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM celebs WHERE firstname="Angelina"''')
    row = c.fetchone()
    conn.close()
    #return

    return render_template('view_one_celeb.htm', celebID=row[0], firstname=row[1], lastname=row[2], age=row[3], email=row[4], photo=row[5], bio=row[6])

def get(request):
    pass

def post(request):
    pass

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.run(debug=False)

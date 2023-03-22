from flask import Flask, render_template, request
from uuid import uuid4
import sqlite3

#Savienojas ar datubāzi
db= sqlite3.connect('ValstsKartes.db', check_same_thread=False)
cur= db.cursor()

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("about.html")
#No datubāzes nolasa datus un izvada to html failā
@app.route("/galvena", methods=['POST', 'GET'])
def galvena():
    sad1 = (""" SELECT * FROM karte""")
    cur. execute(sad1)
    data= cur.fetchall()
    if request.method == 'POST':
        ievads= request.form['ievads']
    return render_template("galvena.html", data=data)

@app.route("/karte", methods=['POST', 'GET'])
def kartes():
    if request.method == 'POST':
        ievads= request.form['ievads']
        sad1 = (""" SELECT * FROM karte WHERE valsts=?""")
        cur.execute(sad1, (ievads,))
        data= cur.fetchall()
        url = data[0][2]
        print(url)
    return render_template("karte.html", url=url)  

@app.route("/about")
def about():
    return render_template("about.html") 


if __name__=="__main__":
   app.run(debug=True)
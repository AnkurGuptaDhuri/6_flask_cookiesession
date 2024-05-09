from flasksessionpackage import app
from flask import render_template, request, redirect, url_for, make_response, session


@app.route("/")
def index():
    return render_template('index.html')
 
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['fname']  + request.form['lname']
        print(username)
        res = make_response(redirect(url_for('home'))) #f"<h1> Welcome to {username} </h1>")
        session["username"] = username
        res.set_cookie('email',request.form['email'])
        return(res) #f"<h1> Welcome to {{username}} </h1>"
        #redirect(url_for('home'))

    return render_template("login.html")

@app.route("/home", methods=['GET'])
def home():
    print("home function")
    if session.get("username", None):
        myuser = session.get('username', None)
        email = request.cookies.get('email', None)
        return f"<h1> Welcome to {myuser} . Successfully logged in for {email}</h1>"
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session["username"] = None
    session.pop('username')
    return redirect("/")
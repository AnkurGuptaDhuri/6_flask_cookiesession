from flask import Flask
from flask import session
from flask_session import Session

app = Flask(__name__, template_folder='templates')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key ="secretkey123"
Session(app)

from flasksessionpackage  import routes


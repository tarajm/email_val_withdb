from flask import Flask
app = Flask(__name__)
app.secret_key = "baboo"

from flask_app.controllers import users
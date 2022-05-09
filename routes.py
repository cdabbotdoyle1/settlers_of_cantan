from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from authmechanism import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

@app.route('/')
def homepage():
    return "Hello world"




@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

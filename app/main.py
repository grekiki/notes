from flask import Flask
from model import Model

app = Flask(__name__)
m = Model()

@app.route('/main')
def hello_world():
    return m.output
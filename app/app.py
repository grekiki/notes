from flask import Flask, request
from model import Model
import random

app = Flask(__name__)
m = Model()

@app.route('/main')
def hello_world():
    ip = request.access_route[0]
    print(ip)
    m.update(str(ip))
    return m.get_output()

from flask import Flask, request
import random
import os

class Model:
    def __init__(self):
        pass

    def update(self, s):
        if os.path.exists("cache/" + s + ".txt"):
            curr = int(open("cache/" + s + ".txt","r").read())

            with open("cache/" + s + ".txt","w") as f:
                f.write(str(curr+1) + "\n")

        else:
            with open("cache/" + s + ".txt","w") as f:
                f.write("0\n")

    def get_output(self):
        output = ""
        try:
            for f in os.listdir("cache"):
                print(f)
                output += f + "<br>"
            output += "Hello world!"
        except Exception:
            return "Cache folder issues"
        return output

app = Flask(__name__)
m = Model()

@app.route('/main')
def hello_world():
    ip = request.access_route[0]
    print(ip)
    m.update(str(ip))
    return m.get_output()

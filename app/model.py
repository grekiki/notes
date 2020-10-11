import os

class Model:
    def __init__(self):
        pass

    def update(self, s):
        if os.path.exists("app/cache/" + s + ".txt"):
            curr = int(open("app/cache/" + s + ".txt","r").read())

            with open("app/cache/" + s + ".txt","w") as f:
                f.write(str(curr+1) + "\n")

        else:
            with open("app/cache/" + s + ".txt","w") as f:
                f.write("0\n")

    def get_output(self):
        output = ""
        try:
            for f in os.listdir("app/cache"):
                print(f)
                output += f + "<br>"
            output += "Hello world!"
        except Exception:
            return "Cache folder issues"
        return output
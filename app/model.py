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
                f.write("100\n")

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
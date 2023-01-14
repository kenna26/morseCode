from flask import Flask, render_template, request
import sys
sys.path.insert(0, '/user/kennaschneider/Documents/morseCode.morseCode.py')
from morseCode import translateBoth


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/translate", methods = ["GET", "POST"])
def translate():
    if request.method == "POST":
        output = request.form["input"]
        newText = translateBoth(output)
        return render_template("main.html", output = newText)
    else:
        return render_template("main.html")


#________________________
#     Methods and Shit
#_________________________


if __name__ == "__main__":
    app.run(debug=True)
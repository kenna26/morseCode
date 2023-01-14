from flask import Flask, render_template, request
import sys
sys.path.insert(0, '/user/kennaschneider/Documents/morseCode.morseCode.py')
from morseCode import translateBoth, translateToMorse
from morseCode import blinker

class Vars():
    audioPlaying = False
    currentMorseCode = ".... ."

app = Flask(__name__)

@app.route("/audio", methods = ["GET", "POST"])
@app.route("/")
def main():
    if request.method == "POST":
        pathList = makeBlinkerList(request.form["play"])
        print(f'list {pathList}')
        return render_template("main.html", pathList = pathList)

    return render_template("main.html")

@app.route("/translate", methods = ["GET", "POST"])
def translate():
    if request.method == "POST":
        output = request.form["input"]
        newText = translateBoth(output)
        Vars.currentMorseCode = translateToMorse(output)
        return render_template("main.html", output = newText)
    else:
        return render_template("main.html")


#________________________
#     Methods and Shit
#_________________________

def makeBlinkerList(text):
    final = []
    
    for char in text:
        if char == ".":
            final.append("{{ url_for('static', filename ='dot.wav') }}")
        elif char == "-":
            final.append("{{ url_for('static', filename ='dash.wav') }}")
        elif char == " ":
            final.append("{{ url_for('static', filename ='silence.wav') }}")
    return final


if __name__ == "__main__":
    app.run(debug=True)
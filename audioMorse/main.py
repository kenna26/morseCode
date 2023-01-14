from flask import Flask, render_template, request
import sys
sys.path.insert(0, '/user/kennaschneider/Documents/morseCode.morseCode.py')
from morseCode import translateBoth, translateToMorse
from morseCode import blinker

class Vars():
    audioPlaying = False
    currentMorseCode = ".... ."

app = Flask(__name__)

@app.route("/")
def main():
    audioPlaying = False
    currentMorseCode = ".... ."
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

#Play and Pause controls
@app.route("/play-pause", methods =["GET", "POST"])
def playPause():
    if not Vars.audioPlaying: #nothing is currently playing 
        Vars.audioPlaying = True
        print(f"now playing: {Vars.currentMorseCode}")
        blinker(Vars.currentMorseCode)
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
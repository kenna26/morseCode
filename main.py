from flask import Flask, render_template, request
from morseCode import translateMorse

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")
    

@app.route("/translate", methods = ["GET", "POST"])
def translate():
    if request.method == "POST":
        output = request.form["input"]
        newText = translateMorse(output)
        return render_template("main.html", output = newText)
    else:
        return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
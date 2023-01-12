from playsound import playsound
from time import sleep

#______Properties_____

morseCode = {"A" : ".-", "B": "-...", "C": "-.-.","D":"-..", "E":".", 
"F":"..-.","G":"--.", "H":"....","I":"..","J":".---","K":"-.-","L":".-..",
"M":"--", "N":"-.","O":"---", "P":".--.","Q":"--.-","R":".-.","S":"...",
"T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..", " ":"/"}

#"/" means space between letters
#"/ " means space between words

#______METHODS_____

def checkLetters(text):
     for element in "qwertyuiopasdfghjklzxcvbnm":
        if (element in text):
            return True

def translateMorse(text):
    final = ""
    if checkLetters(text): #input is english
        first = True
        for letter in text:
            if not first:
                final += " "
            first = False

            if letter == " ":
                final += "/"
            else:
                final += morseCode[letter.upper()]

    else: #input is morse code
        split = text.split(" ")
        for morseLetter in split:
            if morseLetter == "/":
                final += " " 
            else:
                for letter in morseCode:
                    if morseCode[letter] == morseLetter:
                        final += letter
    return final
        
def blinker(text):
    for char in text:
        if char == ".":
            playsound('dot.wav')
        elif char == "-":
            playsound("dash.wav")
        elif char == " " or char == "/":
            sleep(0.5)

    sleep(0.5) #space between . and -



#______Actual Code_____

#blinker(input("Type your message (morse code): \n"))

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
        


#______Actual Code_____

#print(translateMorse(input("Type your message (morse code or english): \n")))

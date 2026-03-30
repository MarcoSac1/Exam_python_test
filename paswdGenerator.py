import string
import random

lunghezza = int(input("inserisci la lunghezza della paswd desiderata!"))

print("""scegli un set di caratteri da qui: \n1. numeri \n2.lettere \n3.caratteri speciali \n4.exit""")

charlist = ""

while True:
    scelta = int(input("scegli un numero: "))
    
    if scelta == "1":
        charlist += string.ascii_letters
    elif scelta == "2":
        charlist += string.digits
    elif scelta == "3":
        charlist += string.punctuation
    elif scelta == "4":
        print("ciaoo")
    else:
        print("perfavore scegli un opzione valida! ")

pwd = []

for i in range(lunghezza):
    
    randomChar = random.choice(charlist)    
    pwd.append(randomChar)

print("la pwd randomica e' " + "".join(pwd))

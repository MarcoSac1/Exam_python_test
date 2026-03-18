import math

def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def divisione(a, b):
    return a / b

def moltiplicazione(a, b):
    return a * b

while True:
    print("""
    1) somma
    2) sottrazione
    3) divisione
    4) moltiplicazione 
    5) per uscire     
    """)

    num = input("Scegli un'operazione da compiere: ")

    if num == "5":
        print("\n Grazie di avermi usato padrone arrivederci !")# mi permette di uscire dal while
        break  

    if num not in ("1", "2", "3", "4"):
        print("operazione scelta non valida, riseleziona oppure premi 5 per terminare!")
        continue  # ci permette di tornare al menu senza chiedere i numeri

    x = int(input("Inserisci il primo numero: "))
    y = int(input("Inserisci il secondo numero: "))

    if num == "1":
        print("il risultato della somma è:", somma(x, y))
    elif num == "2":
        print("il risultato della sottrazione è:", sottrazione(x, y))
    elif num == "3":
        print("il risultato della divisione è:", divisione(x, y))
    elif num == "4":
        print("il risultato della moltiplicazione è:", moltiplicazione(x, y))

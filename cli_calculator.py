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
        print("\nGrazie di avermi usato padrone arrivederci !")
        break

    if num not in ("1", "2", "3", "4"):
        print("operazione scelta non valida, riseleziona oppure premi 5 per terminare!")
        continue

    x = int(input("Inserisci il primo numero: "))
    y = int(input("Inserisci il secondo numero: "))

    if num == "1":
        print(f"il risultato della somma è: {somma(x, y):.2f}")
    elif num == "2":
        print(f"il risultato della sottrazione è: {sottrazione(x, y):.2f}")
    elif num == "3":
        print(f"il risultato della divisione è: { divisione(x, y):.2f}")
    elif num == "4":
        print(f"il risultato della moltiplicazione è: {moltiplicazione(x, y):.2f}")
    continua = input("\nVuoi fare un altro calcolo? (s/n): ").strip().lower()
    if continua == "n":
        print("\nGrazie di avermi usato padrone arrivederci !")
        break

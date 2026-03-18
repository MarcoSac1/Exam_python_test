def somma(a, b):
    return a + b

def sottrazione(a,b):
    return a - b

def divisione (a, b):
    return a / b

def moltiplicazione (a, b):
    return a * b

calc = True

while calc:
    
    print("""
    1) somma
    2) sottrazione
    3) divisione
    4) moltiplicazione 
    5) per uscire     
    """)
    calc = input("Scegli un operazione da compiere: ")
    
    
    x = int(input("Inserisci il primo numero: "))
    y = int(input("Inserisci il secondo numero: "))
    
    if calc == "1":
        print("sommato")
        print("La somma è:", somma(x, y))
    elif calc == "2":
        print("sottrazione")
        print("La sottrazione è:", sottrazione(x, y))
    elif calc == "3":
        print("diviso")
        print("La divisione è:", divisione(x, y))
    elif calc == "4":
        print("moltiplicato")
        print("La moltiplicazione è:", moltiplicazione(x, y))
    elif calc == "5":
        print("grazie di avermi usato padrone arrivederci !")
    else:
        print("operazione scelta non valida ri selezionare!")



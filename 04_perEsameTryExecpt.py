def dividi(n):
    risultato = n / 100
    return risultato

while True:
    try:
        a = int(input("Inserisci un numero: "))
        break
    except ValueError:
        print("Errore..! Inserisci un valore accettato dal programma ")

print("Il risultato della divisione e': ", dividi(a))
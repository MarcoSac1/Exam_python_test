def media(l):
    risultato = sum(l) / len(l)
    return print("la media dei valori nella tua lista e': ", risultato)

n = int(input("Quanti numeri vuoi inserire? "))
l = [] # 1. Crea la lista vuota

for i in range(n): # 2. Cicla n volte
    numero = int(input(f"Inserisci il numero {i+1}: "))
    l.append(numero) # 3. Aggiunge il numero alla lista

print("La tua lista è:", l)

media(l)
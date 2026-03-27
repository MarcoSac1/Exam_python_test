def media(l):
    risultato = sum(l) / len(l)
    return print("la media dei valori nella tua lista e': ", risultato)

n = int(input("Quanti numeri vuoi inserire? "))
l = [] 

for i in range(n): 
    numero = int(input(f"Inserisci il numero {i+1}: "))
    l.append(numero) 

print("La tua lista è:", l)

media(l)
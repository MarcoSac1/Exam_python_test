n = int(input("Quanti numeri vuoi inserire? "))
l = []

for i in range(n):
    numero = int(input(f"Inserisci il numero {i+1}: "))
    l.append(numero) # 3. Aggiunge il numero alla lista

print("lista riempita !" ,l )


for i in range(len(l) - 1):
    risultato = l[i] ** l[i+1]
    print(f"{l[i]} elevato a {l[i+1]} e' : {risultato}")

print("l'ultimo elemento e': ", l [-1])
n = int(input("inserisci il numero di elementi che vuoi inserire: "))

lista = []

for i in range(n):
    lista.append(int(input(f"inserisci numero {i +1}: ")))

print("somma totale: ", sum(lista))

for i in range(len(lista) -1):
    lista[i] = lista[i] ** lista[i + 1]

print("lista finale: ", lista)
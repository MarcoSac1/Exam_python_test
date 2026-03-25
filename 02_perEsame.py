my_lists = ["Catania", "Messina", "Palermo", "Torino", "patti"]

for citta in my_lists:
    if len(citta) > 6: 
        print("città con più di 6 caratteri nel nome !", citta)
    else:
        print("le città con meno di 6 lettere sono: ",citta)

print("Lista originale:---------------------------",my_lists)

my_lists.append("Francoforte")
print("Lista modificata con append:",my_lists)#come modificare una lista con .append


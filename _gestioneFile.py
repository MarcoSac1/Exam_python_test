def appendKey(nome_file, key, value):
    with open(nome_file, "a") as f:
        f.write(f"{key}={value}\n")

files_creati = [] # Lista per memorizzare i nomi dei file

while True:
    print("\n0) Esci\n1) Crea/Aggiorna file\n2) Visualizza file creati\n3) leggi il file")
    scelta = input("Scegli un'operazione: ")

    if scelta == "0":
        break
    elif scelta == "1":
        nome = input("Inserisci il nome del file (.ini): ")
        k = input("Inserisci la chiave: ")
        v = input("Inserisci il valore: ")
        
        appendKey(nome, k, v)
        
        # Aggiungiamo il nome alla lista se non è già presente
        if nome not in files_creati:
            files_creati.append(nome)
            
    elif scelta == "2":
        print("File creati finora:")
        for f in files_creati: # Ciclo per stampare la lista [3]
            print("-", f)
    elif scelta == "3":
        nome_file = input("inserisci il nome del file che vuoi leggere: ")
        try:
            with open(nome_file, "r") as f:
                contenuto = f.read() # Legge tutto il file
                if contenuto:
                        print("Contenuto del file:\n\n", contenuto)
                else:
                    print("Il file è vuoto.")
        except FileNotFoundError:
            print("Errore: il file non esiste!")
    else:
        print("Scelta non valida!")
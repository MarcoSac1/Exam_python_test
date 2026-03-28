import json

def esercizio_json(nome_file):
    try:
        with open(nome_file, "r") as f:
            dati = json.load(f)
        
        # 1. Controlla JSON ORIGINALE prima di modificare
        users_originali = [user.strip().lower() for user in dati["users"]]
        root_presente_originale = "root" in users_originali
        is_modifiable = dati.get("isModifiable", False)
        
        print("\n--- DEBUG ---")
        print(f"Users ORIGINALI: {dati['users']}")
        print(f"'root' nel JSON originale? {root_presente_originale}")
        print(f"isModifiable: {is_modifiable} ({type(is_modifiable)})")
        print("--------------\n")

        # 2. Aggiorna con input utente
        input_utente = input("Inserisci i nomi (es: marco root): ")
        dati["users"] = [n.strip().lower() for n in input_utente.split()]

        # 3. DECIDE dove salvare
        if root_presente_originale:  # SOLO se "root" era già nel JSON
            nome_uscita = "nuovo_" + nome_file
            print(f"🔒 SICUREZZA: 'root' trovato ORIGINALE! Creo '{nome_uscita}'")
        else:
            nome_uscita = nome_file
            print(f"✅ NORMALE: Sovrascrivo '{nome_uscita}'")

        # 4. Salva
        with open(nome_uscita, "w") as f:
            json.dump(dati, f, indent=4)
        print(f"Salvato in: {nome_uscita}")
            
    except Exception as e:
        print(f"Errore: {e}")

# Test
esercizio_json("userDB.json")
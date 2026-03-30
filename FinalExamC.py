import csv
from datetime import datetime

class Prenotazione:
    contatore = 0

    def __init__(self, cliente, camera, check_in, check_out, prezzo_notte, codice=None):
        if codice is None:
            Prenotazione.contatore += 1
            self.__codice = f"PH-{Prenotazione.contatore:05d}"
        else:
            self.__codice = codice
            numero = int(codice.split("-")[1])
            if numero > Prenotazione.contatore:
                Prenotazione.contatore = numero

        self.__cliente = cliente
        self.__camera = camera
        self.__check_in = check_in
        self.__check_out = check_out
        self.__prezzo_notte = prezzo_notte

    def calcola_totale(self):
        notti = (self.__check_out - self.__check_in).days
        return notti * self.__prezzo_notte

    def modifica_date(self, nuova_data):
        if nuova_data <= self.__check_in:
            print("Data non valida")
        else:
            self.__check_out = nuova_data

    def get_codice(self):
        return self.__codice

    def to_csv(self):
        return [self.__codice, self.__cliente, self.__camera, self.__check_in, self.__check_out, self.__prezzo_notte]

    def __str__(self):
        notti = (self.__check_out - self.__check_in).days
        totale = self.calcola_totale()
        return (f"[{self.__codice}] {self.__cliente} - Camera {self.__camera}\n"
                f"Check-in: {self.__check_in} | Check-out: {self.__check_out}\n"
                f"{notti} notti x {self.__prezzo_notte:.2f} EUR = {totale:.2f}EUR")

    def __repr__(self):
        return self.__str__()  

prenotazioni = []

with open("prenotazioni.csv", "r+", newline="", encoding="utf-8") as f:
    lettore = csv.DictReader(f, skipinitialspace=True)
    lettore.fieldnames = [campo.strip() for campo in lettore.fieldnames]

    for riga in lettore:
        p = Prenotazione(
            riga["Cliente"].strip(),
            riga["Camera"].strip(),
            datetime.fromisoformat(riga["CheckIn"].strip()),
            datetime.fromisoformat(riga["CheckOut"].strip()),
            float(riga["PrezzoNotte"].strip()),
            riga["Codice"].strip()
        )
        prenotazioni.append(p)

def inserisci_prenotazione():
    cliente = input("cliente: ")
    camera = input("camera: ")
    check_in = datetime.fromisoformat(input("Check-in (YYYY-MM-DD): "))
    check_out = datetime.fromisoformat(input("Check-out (YYYY-MM-DD): "))
    prezzo_notte = float(input("Prezzo notte: "))

    if check_out <= check_in:
        print("Data non valida")
        return

    p = Prenotazione(cliente, camera, check_in, check_out, prezzo_notte)
    prenotazioni.append(p)
    print("Prenotazione inserita")

def modifica_checkout():
    codice = input("Codice prenotazione: ")
    for p in prenotazioni:
        if p.get_codice() == codice:
            nuova_data = datetime.fromisoformat(input("Nuovo check-out (YYYY-MM-DD): "))
            p.modifica_date(nuova_data)
            return
    print("Prenotazione non trovata")

def stampa_prenotazione():
    codice = input("Codice prenotazione: ")
    for p in prenotazioni:
        if p.get_codice() == codice:
            print(p)
            return
    print("Prenotazione non trovata")

def stampa_tutte():
    for p in prenotazioni:
        print(p)
        print()

def cancella_prenotazione():
    codice = input("Codice prenotazione da cancellare: ")
    for i, p in enumerate(prenotazioni):
        if p.get_codice() == codice:
            prenotazioni.pop(i)
            print("Prenotazione cancellata")
            return
    print("Prenotazione non trovata")

def salva_prenotazione():
    with open("prenotazioni.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Codice", "Cliente", "Camera", "CheckIn", "CheckOut", "PrezzoNotte"])
        for p in prenotazioni:
            writer.writerow(p.to_csv())
    print("File salvato")

def __str__ ( self ) :
    notti = ( self . __check_out - self . __check_in ) . days
    totale = self . calcola_totale ()
    return ( f"[{ self . __codice }] { self . __cliente } - Camera { self . __camera }\n"f"Check -in: { self . __check_in } | Check - out:{ self . __check_out }\n"f"{ notti } notti x { self . __prezzo_notte :.2f} EUR = { totale :.2f}EUR")
def __repr__ ( self ) :
    return self . __str__ ()

while True:
    print("""\nScegli un operazione da compiere:\n 1. inserisci prenotazione\n 2. Modifica Data check-out\n 3. Stampa singola prenotazione\n 4. Stampa tutte le prenotazioni\n 5. Cancella prenotazione\n 6. Salva prenotazioni su file\n 7. Esci""")
    scelta = int(input("Inserisci il numero del azione da compiere: \n"))
    
    if scelta == 1:
        inserisci_prenotazione()
    elif scelta == 2:
        modifica_checkout()
    elif scelta == 3:
        stampa_prenotazione()
    elif scelta == 4:
        stampa_tutte()
    elif scelta == 5:
        cancella_prenotazione()
    elif scelta == 6:
        salva_prenotazione()
    elif scelta == 7:
        print("Grazie ed arrivederci")
        break
    else:
        print("scelta non valida selezionare un opzione valida!")
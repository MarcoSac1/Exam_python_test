esame = [
    {"studente" : "Franco","Materia" : "Filosofia","Voto" : 30},
    {"studente" : "Carlo","Materia" : "storia","Voto" : 16}
]

for s in esame:
    if s ["Voto"] >= 18:
        print(f"{s['studente']} è Promosso in {s['Materia']} il suo voto e' {s['Voto']}!") #l'uso di fstrin e importante per migliorare la visualizazione dei dati 
    else:
        print(f"{s['studente']} è Bocciato in {s['Materia']} il suo voto e' {s['Voto']}.")
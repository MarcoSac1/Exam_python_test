def coefficienti():
    """Inserisce coefficienti da input"""
    coef = input("Inserisci i coefficienti (es: 1 2 3 -4 separati da spazio): ")
    split_coef = [float(x) for x in coef.split()]
    return split_coef

def ruffini(coeffs, k):
    """Applica metodo Ruffini: divisione polinomio / (x - k)"""
    f = coeffs[:]
    n = len(f) - 1
    i = n - 1
    while i >= 0:
        f[i] = f[i] + f[i + 1] * k 
        i -= 1
    r = f[0]
    q = f[1:]
    return q, r

# Menu principale
while True:
    print("""
    0) Esci dalla calcolatrice.
    1) Ruffini
    """)
    scelta = input("Scegli: ")
    
    if scelta == "0":
        print("Grazie! Arrivederci!")
        break
    
    if scelta == "1":
        coeffs = coefficienti()
        k = float(input("Inserisci k per (x - k): "))
        q, r = ruffini(coeffs, k)
        print("Quoziente:", q)
        print("Resto:", r)
        if r == 0:
            print("k è radice del polinomio!")
    else:
        print("Scelta non valida!")

import math

punto_a = (10, 20) 
punto_b = (60, 37)

def distanza (a, b):
    differenza_A = (a[0] - b[0]) ** 2
    differenza_B = (a[1] - b[1]) ** 2
    distanza = math.sqrt(differenza_A + differenza_B)
    print("misurazione punti catastali: ", a, b)
    print(f"la distanza tra il punto A:{a} ed il punto B{b} e' di: {distanza: .2f}\n")


def quadrato(a, b):
    quadrato_A = (a[0] - b[0]) ** 2
    quadrato_B = (a[1] - b[1]) ** 2
    quad = (quadrato_A + quadrato_B)
    print(f"il quadrato della distanza delle due misurazioni A{a} e B{b} e' di : {quad: .2f}\n")

while True:
    print("0) Esci\n1) Distanza\n2) Quadrato della distanza")
    scelta = input("Scegli un operazione da compiere: ")
    
    if scelta == "0":
        break
    elif scelta =="1":
        distanza(punto_a, punto_b)
    elif scelta =="2":
        quadrato(punto_a, punto_b)
    else:
        print("Scelta non valida seleziona un operazione da compiere o esci con 0\n")




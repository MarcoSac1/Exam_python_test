import math

punto_a = (10, 20) 
punto_b = (60, 37)

print("misurazione punti catastali: ", punto_a, punto_b)

differenza_A = (punto_a[0] - punto_a[1]) ** 2
differenza_B = (punto_b[0] - punto_b[1]) ** 2

distanza = math.sqrt(differenza_A + differenza_B)
print("la distanza tra i due punti e' di: ", distanza)
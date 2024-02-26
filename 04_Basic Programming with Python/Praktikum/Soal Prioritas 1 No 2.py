# Buatlah sebuah program untuk menghitung volume bola. Volume tabung dapat dihitung dengan rumus berikut: V = 4/3 * phi * r^3
# Catatan: gunakan nilai Phi  = 3.14

def volumeBola(r):
   result = (4 * 3.14 * r * r * r)/3
   print(f"Volume bola: {result:.3f}")
   
r = 7
volume = volumeBola(r)
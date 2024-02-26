# Buatlah sebuah program untuk menghitung luas persegi panjang. Kemudian dari hasil perhitungan luas tersebut tampilkan tulisan “even rectangle” jika luas merupakan bilangan genap dan tampilkan tulisan “odd rectangle” jika luas merupakan bilangan ganjil. Rumus perhitungan luas persegi panjang adalah sebagai berikut: L = p * l

def luasPersegiPanjang(length, width):
   result = length * width
   if result % 2 == 0:
      print(f"Area result: {result}, it is even rectangle.")
   else:
      print(f"Area result: {result}, it is odd rectangle.")

length1 = 4
width1 = 6
luasPersegiPanjang(length1, width1)
length2 = 7
width2 = 5
luasPersegiPanjang(length2, width2)
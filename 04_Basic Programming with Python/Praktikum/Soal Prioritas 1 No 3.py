"""
Buatlah sebuah program yang mencetak angka dari 1 sampai 100 dengan kriteria sebagai berikut:
a. Jika bilangan merupakan kelipatan 3 maka tampilkan hasil kuadrat dari bilangan tersebut.
b. Jika bilangan merupakan kelipatan 5 maka tampilkan hasil perpangkatan 3 dari bilangan tersebut.
c. Jika bilangan merupakan kelipatan 3 dan 5 maka tampilkan tulisan “buzz”
d. Jika tiga kriteria diatas tidak terpenuhi maka tampilkan bilangan aslinya.
"""

def cetakBilangan(n):
   for i in range(1, n+1):
      if i % 3 == 0 and i % 5 == 0:
         print("buzz")
      elif i % 3 == 0:
         print(i * i)
      elif i % 5 == 0:
         print(i * i * i)
      else:
         print(i)
         
cetakBilangan(100)
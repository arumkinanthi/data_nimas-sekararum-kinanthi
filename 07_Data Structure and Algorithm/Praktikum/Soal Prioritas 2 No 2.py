"""
Buatlah segiempat berukuran height x width yang berisikan bilangan-bilangan prima setelah start, pada bagian akhir jumlahkan seluruh bilangan prima tersebut.
"""

def prime_rectangle(width, height, start):
   prime_sum = 0
   print("Hasil: ")
   # lines loop
   for i in range (height):
      # colums loop
      for j in range (width):
         while True:
            pembagi = 0
            start += 1
            # checking the divider(s)
            for k in range (1, start + 1):
               if start % k == 0:
                  pembagi += 1
            # checking the prime(s)
            if pembagi == 2:
               print(start, end = " ")
               prime_sum += start
               # breaking the loop if the divisors add up to 2 numbers
               break
      # separating the columns of each lines
      print(" ")
   # show the total sum of the prime(s)
   print("Hasil penjumlahan seluruh bilangan prima:", prime_sum)
   
def menu():
   width = int(input("Masukkan jumlah baris: "))
   height = int(input("Masukkan jumlah kolom: "))
   start = int(input("Masukkan sebuah bilangan acuan: "))
   prime_rectangle(width, height, start)
   
menu()
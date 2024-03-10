"""
Buatlah sebuah program untuk memasukkan sekumpulan karakter dari sebuah kata berdasarkan ruangan yang tersedia. Mekanisme dapat dilihat pada gambar berikut:

Test Case 1:
Input:
   Word: alta
   Rooms: 10
Output: altaaltaal

Test Case 2:
Input:
   Word: sepulsa
   Rooms: 20
Output: sepulsasepulsasepuls
"""

def collect_chars(word, rooms):
   listed_word = list(word.replace(" ", ""))
   appended_letter = []
   string = ""
   count = 0 
   # putting the letter into the available room
   for i in range (rooms):
      appended_letter.append(listed_word[count])
      # menjadikan nilai count sebagai 0 pada setiap kelipatan yang sesuai dengan jumlah huruf pada input agar huruf dimasukkan kembali dari awal jika masih ada ruang kosong
      if (i+1) % len(listed_word) == 0 and i > 0:
         count = 0
      else:
         count += 1
   # returning the string
   return string.join(appended_letter)

def menu():
   print("Program Karakter")
   word = input("Masukkan kata/kalimat: ")
   rooms = int(input("Masukkan jumlah kolom yang tersedia: "))
   print("Hasil:", collect_chars(word, rooms))
   
menu()
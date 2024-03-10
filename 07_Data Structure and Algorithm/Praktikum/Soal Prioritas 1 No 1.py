"""
Buatlah sebuah program untuk mengelompokkan sekumpulan bilangan berdasarkan target kelipatan yang diinginkan:

Test Case 1:
Input:
   Numbers: [1,2,3,4,5,6,7,8,9]
   Target: 3
Output: [[3, 6, 9], [1, 2, 4, 5, 7, 8]]

Test Case 2:
Input:
   Numbers: [23,15,19,20,75,30,45]
   Target: 5
Output: [[15, 20, 75, 30, 45], [23, 19]]    
"""

def group_numbers(numbers, target):
   kelipatan = []
   bukan_kelipatan = []
   # checking multiple of the target in the list
   for i in range (len(numbers)):
      if numbers[i] % target == 0:
         kelipatan.append(numbers[i])
      else:
         bukan_kelipatan.append(numbers[i])
   # returning the list
   return [kelipatan, bukan_kelipatan]

def menu():
   numbers = []
   print("Tekan Enter jika sudah selesai memasukkan semua bilangan.")
   while True:
      number = input("Masukkan bilangan yang diinginkan: ")
      if number == '':
         break
      numbers.append(int(number))
   print("Anda menekan Enter, penginputan bilangan telah selesai.\nDaftar bilangan yang sudah Anda masukkan:", numbers)
   target = int(input("Masukkan target yang diinginkan: "))
   print("Hasil:", group_numbers(numbers, target))

menu()
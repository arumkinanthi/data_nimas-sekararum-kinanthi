import sys

for line in sys.stdin:
   # menghapus whitespace di sekitar string
   line = line.strip()
   # memecah baris menjadi list kata
   words = line.split()
   # menghasilkan pasangan (key, value) untuk setiap kata
   for word in words:
      # mengirim kata dan status palindrom (True/False) ke reducer
      is_palindrome = word == word[::-1]
      print(word, is_palindrome)

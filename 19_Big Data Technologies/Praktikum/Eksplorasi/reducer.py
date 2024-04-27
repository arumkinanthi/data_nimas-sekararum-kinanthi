import sys

for line in sys.stdin:
   # memecah baris menjadi kata dan status palindrom
   word, is_palindrome_str = line.split()
   is_palindrome = is_palindrome_str.lower() == 'true'

   # menampilkan "True" atau "False" berdasarkan status palindrom
   print(str(is_palindrome))

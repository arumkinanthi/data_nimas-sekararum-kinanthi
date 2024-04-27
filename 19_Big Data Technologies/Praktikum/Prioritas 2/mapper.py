import sys

for line in sys.stdin:
   # menghapus whitespace di sekitar string
   line = line.strip()
   # memecah baris menjadi list angka
   numbers = line.split()
   # menghasilkan pasangan (key, value) untuk setiap angka
   for number in numbers:
      print("total", float(number))
      print("count", 1)

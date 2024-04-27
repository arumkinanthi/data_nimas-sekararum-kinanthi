import sys

total_sum = 0
count_sum = 0

for line in sys.stdin:
   # memecah baris menjadi key dan value
   key, value = line.split()
   value = float(value)

   # menghitung total dan jumlah angka
   if key == "total":
      total_sum += value
   elif key == "count":
      count_sum += value

# menghitung nilai mean
mean = total_sum / count_sum
print("Mean:", mean)

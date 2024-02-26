"""
Buatlah sebuah program untuk menentukan tarif pengiriman paket berdasarkan berat paket dan jarak yang ditempuh dengan spesifikasi berikut:

|Berat   |Tarif   |
|1 - 20  |10000   |
|21 - 30 |15000   |
|31 - 60 |20000   |
|> 60    |45000   |

|Jarak   |Tarif   |
|1 - 5   |2000    |
|6 - 15  |5000    |
|16 - 30 |10000   |
|> 30    |15000   |

Tarif keseluruhan = tarif berdasarkan berat + tarif berdasarkan jarak

Input:
- Berat: 24
- Jarak: 10
Output: 20000

Input:
- Berat: 20
- Jarak: 40
Output: 25000
"""

def tarifBerat(weight):
   if (1 <= weight <= 20):
      tarif = 10000
   elif (21 <= weight <= 30):
      tarif = 15000
   elif (31 <= weight <= 60):
      tarif = 20000
   elif (weight > 60):
      tarif = 45000
   return tarif

def tarifJarak(distance):
   if (1 <= distance <= 5):
      tarif = 20000
   elif (6 <= distance <= 15):
      tarif = 5000
   elif (16 <= distance <= 30):
      tarif = 10000
   elif (distance > 30):
      tarif = 15000
   return tarif

berat1 = 24
jarak1 = 10
totalTarif1 = tarifBerat(berat1) + tarifJarak(jarak1)
print(f"Total tarif pertama: {totalTarif1}")

berat2 = 20
jarak2 = 40
totalTarif2 = tarifBerat(berat2) + tarifJarak(jarak2)
print(f"Total tarif kedua: {totalTarif2}")
"""
Buatlah sebuah program untuk menentukan prioritas dari sebuah proyek berdasarkan budget, waktu pengerjaan dan tingkat kesulitan. Kriteria dari penentuan proyek adalah menggunakan skor secara keseluruhan. Perhitungan skor dari setiap faktor tersebut dihitung dengan kriteria berikut:

|Budget  |Skor |
|0 - 50  |4    |
|51 - 80 |3    |
|81 - 100|2    |
|> 100   |1    |

|Waktu Pengerjaan |Skor |
|0 - 20           |4    |
|21 - 30          |3    |
|31 - 50          |2    |
|> 50             |1    |

|Tungkat Kesulitan|Skor |
|0 - 3            |4    |
|4 - 6            |3    |
|8 - 10           |2    |
|> 10             |1    |

Hasil prioritas proyek diambil dari skor yang sudah dihitung.
|Skor    |Hasil      |
|24 - 17 |High       |
|16 - 10 |Medium     |
|9 - 3   |Low        |
|<= 2    |Impossible | 

Test case:
Input:
- Budget: 40
- Waktu pengerjaan: 25
- Tingkat kesulitan: 5
Output: Medium

Input:
- Budget: 51
- Waktu pengerjaan: 10
- Tingkat kesulitan: 3 
Output: High
"""

def budget(dana):
   if 0 <= dana <= 50:
      score = 4
   elif 51 <= dana <= 80:
      score = 3
   elif 81 <= dana <= 100:
      score = 2
   elif dana > 100:
      score = 1
   return score

def waktu(duration):
   if 0 <= duration <= 20:
      score = 10
   elif 21 <= duration <= 30:
      score = 5
   elif 31 <= duration <= 50:
      score = 2
   elif duration > 50:
      score = 1
   return score

def kesulitan(difficulty):
   if 0 <= difficulty <= 3:
      score = 10
   elif 4 <= difficulty <= 6:
      score = 5
   elif 8 <= difficulty <= 10:
      score = 1
   elif difficulty > 10:
      score = 0
   return score

def totalScore(dana, duration, difficulty):
   total_score = budget(dana) + waktu(duration) + kesulitan(difficulty)
   print(f"Total skor: {total_score}") # print total score
   if 17 <= total_score <= 24:
      result = "High"
   elif 10 <= total_score <= 16:
      result = "Medium"
   elif 3 <= total_score <= 9:
      result = "Low"
   elif total_score <= 2:
      result = "Impossible"
   print(f"Priority: {result}")
   print("")

budget1 = 40
duration1 = 25
difficulty1 = 5
totalScore(budget1, duration1, difficulty1)

budget2 = 51
duration2 = 10
difficulty2 = 3
totalScore(budget2, duration2, difficulty2)
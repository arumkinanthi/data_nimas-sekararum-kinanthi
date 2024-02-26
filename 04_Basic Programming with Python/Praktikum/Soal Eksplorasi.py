"""
Buatlah sebuah program untuk memeriksa apakah sebuah kata adalah anagram dari suatu kata yang lain. Anagram merupakan sebuah kata yang memiliki frekuensi huruf yang sama dengan kata lain.
Contoh dari anagram adalah sebagai berikut:      
a. Kata pulsa merupakan anagram dari kata palsu karena jumlah frekuensi huruf pada dua kata tersebut adalah sama.
b. Kata kasur merupakan anagram dari kata rusak karena jumlah frekuensi huruf pada dua kata tersebut adalah sama.
c. Kata donat bukan merupakan anagram dari kata donatello karena jumlah frekuensi huruf pada dua kata tersebut beda.

Test case
Input:
- Kata pertama: kasur
- Kata kedua: rusak
Output: Anagram
Pembahasan: kata kasur merupakan anagram dari kata rusak karena jumlah frekuensi huruf pada dua kata tersebut adalah sama.

Input:
- Kata pertama: donat
- Kata kedua: tandon
Output: Bukan Anagram
Pembahasan: kata donat bukan merupakan anagram dari kata tandon karena jumlah frekuensi huruf pada dua kata tersebut berbeda.
"""

def sorting(string):
   sorted_string = sorted(string)
   joined_string = "".join(sorted_string)
   return joined_string

def areAnagram(string1, string2):
   sorted1 = sorting(string1)
   sorted2 = sorting(string2)
   if (sorted1 == sorted2):
      print(f"Anagram\nPembahasan: Kata {string1} merupakan anagram dari kata {string2} karena jumlah frekuensi huruf pada dua kata tersebut adalah sama.")
   else:
      print(f"Bukan Anagram\nPembahasan: Kata {string1} bukan merupakan anagram dari kata {string2} karena jumlah frekuensi huruf pada dua kata tersebut berbeda.")
   
string1 = "pulsa"
string2 = "palsu"
areAnagram(string1, string2)

string1 = "kasur"
string2 = "rusak"
areAnagram(string1, string2)

string1 = "donat"
string2 = "tandon"
areAnagram(string1, string2)
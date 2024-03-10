"""
Sebuah perusahaan roti ingin menentukan jenis roti yang dibuat berdasarkan jumlah tepung yang tersedia. Buatlah sebuah program untuk menentukan jenis roti yang dapat dibuat berdasarkan jumlah tepung yang tersedia.

Test Case 1:
Input:
   Flour stock: 100
   Breads: [{"name":"donut","flour":25},{"name":"mini puff","flour":15},{"name":"baguette","flour":75},{"name":"cupcake","flour":15}]
Output:
   tampilkan jenis roti yang dapat dibuat
   ['mini puff', 'cupcake', 'donut']
"""

def get_breads(breads, flour_stock):
   # sorting
   for i in range (len(breads)):
      for j in range (len(breads)-1):
         if breads[j]['flour'] > breads[j+1]['flour']:
            breads[j], breads[j+1] = breads[j+1], breads[j]
   # checking which bread could be made
   avail_breads = []
   sum, i = 0, 0
   while sum + breads[i]['flour'] <= flour_stock:
      sum += breads[i]['flour']
      avail_breads.append(breads[i]['name'])
      i += 1
   #returning the bread
   print("Amount of used flour:", sum)
   print("The bread list:")
   return avail_breads

def menu():
   bread_list = []
   bread_flour = []
   print("Please press Enter when you are done entering the breads name.")
   while True:
      name = input("Enter bread name\t: ")
      if name == "":
         break
      flour = int(input("Enter flour amount\t: "))
      bread_flour = {'name': name, 'flour': flour}
      bread_list.append(bread_flour)
   print("You have pressed Enter, the bread name and flour amount entry has been completed.\nThe list you have entered:", bread_list)
   flour = int(input("Enter the flour stock: "))
   print(get_breads(bread_list, flour))

menu()
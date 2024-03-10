"""
Buatlah sebuah program sederhana untuk mengelola data pengeluaran. Fitur program terdiri dari:
Menambahkan data pengeluaran.
Melihat semua data pengeluaran beserta total pengeluaran secara keseluruhan.
Mengubah data pengeluaran.
Menghapus data pengeluaran.
        
Berikut adalah kriteria tambahan:
Menggunakan UUID sebagai identifier data pengeluaran. Untuk cara membuat UUID di Python bisa dilihat disini.
"""
import uuid

data = []

def show(i):
   print("ID\t:", data[i]['id'])
   print("Name\t:", data[i]['name'])
   print("Amount\t:", data[i]['amount'])

def create():
   data.append({'id': str(uuid.uuid4()), 'name' : input("Enter expense name\t: "), 'amount' : int(input("Enter expense amount\t: "))})
   print("Data has been added!")
   menu()
   
def view():
   total = 0
   print("========= All Your Expenses =========")
   if not data:
      print("There's no expense(s)")
   else: 
      for i in range (len(data)):
         show(i)
         total += data[i]['amount']
         print("=====================================")
   print("-> TOTAL: Rp", total)
   menu()

def update():
   update_id = input("Enter expense ID\t: ")
   print("=====================================")
   status = False
   for i in range (len(data)):
      if data[i]['id'] == update_id:
         status = True
         show(i)
         data[i]['name'] = input("Enter updated expense name\t: ")
         data[i]['amount'] = int(input("Enter updated expense amount\t: "))
         print("Data has been updated!")
   if status == False:
      print("Data can not be founded!")
   menu()

def delete():
   delete_id = input("Enter expense ID\t: ")
   print("=====================================")
   status = False
   for i in range (len(data)):
      if data[i]['id'] == delete_id:
         print("Data has been founded!")
         show(i)
         status = True
         pilihan = input("Are you sure want to delete this data? (y/n): ")
         if pilihan.upper() == "Y":
            del data[i]
            print("Data has been deleted!")
            break
   if status == False:
      print("Data can not be founded!")
   menu()

def exit():
   print("Thank you for trusting me, good bye!")
   return

def menu():
   print("=============== MENU ================")
   print("1. Create new expense data\n2. View expenses\n3. Update expense\n4. Delete expense\n5. Exit")
   print("=====================================")
   choice = int(input("Enter your choice\t: "))
   match choice:
      case 1:
         create()
      case 2:
         view()
      case 3:
         update()
      case 4:
         delete()
      case 5:
         exit()
     
menu()
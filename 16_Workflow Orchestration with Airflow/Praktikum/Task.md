## Soal Prioritas 1 (80)

1. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

   Catatan:
   - Satu task menggambarkan perintah bash yang harus dijalankan.
   - Gunakan BashOperator dalam membuat DAG.\
   Jawab:
   - ![alt text]()


2. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

   Kriteria yang harus dipenuhi:
   - Task pertama adalah membuat sekumpulan bilangan acak dari 1 sampai 50 dengan jumlah bilangan adalah 25 bilangan.
   - Task kedua adalah menghitung jumlah dari semua bilangan yang didapatkan dari task pertama.
   - Task terakhir adalah menentukan apakah jumlah dari semua bilangan merupakan bilangan genap atau bukan. Jika merupakan bilangan genap tampilkan tulisan “Even Sum”. Jika tidak maka tampilkan tulisan “Odd Sum”.
   - Gunakan X-COM dalam proses pertukaran data antar task.
   - Gunakan PythonOperator dalam membuat DAG.
   
   
   
## 📚 Soal Prioritas 2 (20)
Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:       

Kriteria yang harus dipenuhi:
- Task pertama bertujuan untuk mendapatkan data dari API. Berikut adalah endpoint API yang digunakan: https://fakestoreapi.com/products 
- Task kedua bertujuan untuk menulis hasil dari response API ke dalam file CSV
- Task ketiga bertujuan untuk menulis hasil dari response API ke dalam file txt.
- Task terakhir bertujuan untuk menampilkan pesan “done!” untuk menyatakan tugas telah selesai.
- Gunakan Operator berdasarkan jenis task yang dijalankan.
   
   
   
## 📚 Soal Eksplorasi (20)
Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:

Kriteria yang harus dipenuhi:
- Task pertama bertujuan untuk membuat tabel dengan nama fruits untuk menyimpan data buah-buahan.
- Task kedua bertujuan untuk mendapatkan data dari API. Endpoint API yang digunakan adalah sebagai berikut: https://www.fruityvice.com/api/fruit/family/Rosaceae 
- Task ketiga bertujuan untuk memasukkan data buah-buahan ke dalam tabel fruits yang sudah dibuat.
- Gunakan Operator berdasarkan jenis task yang dijalankan.
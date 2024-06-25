## 📚 Soal Prioritas 1

1. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:
   ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/Soal/dag_exercise.png?raw=true)\
   Catatan:
   - Satu task menggambarkan perintah bash yang harus dijalankan.
   - Gunakan BashOperator dalam membuat DAG.\
   Jawab:\
      DAG:
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/prioritas1_1_a.png?raw=true)\
      Output:
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/prioritas1_1_b.png?raw=true)

2. Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:
   ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/Soal/DAG_EXEC_FIX_02.png?raw=true)\
   Kriteria yang harus dipenuhi:
   - Task pertama adalah membuat sekumpulan bilangan acak dari 1 sampai 50 dengan jumlah bilangan adalah 25 bilangan.
   - Task kedua adalah menghitung jumlah dari semua bilangan yang didapatkan dari task pertama.
   - Task terakhir adalah menentukan apakah jumlah dari semua bilangan merupakan bilangan genap atau bukan. Jika merupakan bilangan genap tampilkan tulisan “Even Sum”. Jika tidak maka tampilkan tulisan “Odd Sum”.
   - Gunakan X-COM dalam proses pertukaran data antar task.
   - Gunakan PythonOperator dalam membuat DAG.
   Jawab:\
      DAG:
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/prioritas1_2_a.png?raw=true)\
      Output 1:
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/prioritas1_2_b.png?raw=true)\
      Output 2:
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/prioritas1_2_c.png?raw=true)\
      Output 3:
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/prioritas1_2_d.png?raw=true)\
      Output 4:
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/prioritas1_2_e.png?raw=true)
   
   
## 📚 Soal Prioritas 2
Buatlah sebuah DAG dengan menggunakan Apache Airflow berdasarkan gambar berikut:       
![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/Soal/dag_exec_03.png?raw=true)\
Kriteria yang harus dipenuhi:
- Task pertama bertujuan untuk mendapatkan data dari API. Berikut adalah endpoint API yang digunakan: https://fakestoreapi.com/products 
- Task kedua bertujuan untuk menulis hasil dari response API ke dalam file CSV
- Task ketiga bertujuan untuk menulis hasil dari response API ke dalam file txt.
- Task terakhir bertujuan untuk menampilkan pesan “done!” untuk menyatakan tugas telah selesai.
- Gunakan Operator berdasarkan jenis task yang dijalankan.
Jawab:\
   DAG:
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/prioritas2_a.png?raw=true)\
   Output:
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/17_Workflow%20Orchestration%20with%20Airflow/Screenshot/prioritas2_b.png?raw=true)
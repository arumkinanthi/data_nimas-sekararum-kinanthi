1. Persiapan Lingkungan Pengembangan
   ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/Soal/1.png?raw=true)
   - Buat virtual environment dengan Python dan namai sebagai venv_code untuk mengisolasi proyek.
      ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/1%20a.png?raw=true)
   - Download dataset ChatGPT Sentiment Analysis dari tautan ini kemudian simpan kedalam folder data_source, yang terdiri dari atribut tweets sebagai teks tweet dan label yang merupakan penanda sentimen (good, bad, neutral).
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/1%20b%20(a).png?raw=true)
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/1%20b%20(b).png?raw=true)

2. Persiapan dan Pemrosesan Dataset dengan OOP
   ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/Soal/2.png?raw=true)
   - Bangun class SentimentClassifier dalam Python didalam file sentiment_classifier.py yang memiliki metode untuk membaca dan memproses dataset.
      ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/2%20a.png?raw=true)
      - Metode load_data() akan membaca dataset ke dalam struktur data yang sesuai.
      - Metode classify_sentiment() akan membagi tweets ke dalam kategori good, bad, atau neutral.
      - Metode save_to_csv() akan menyimpan tweets yang diklasifikasikan ke dalam file CSV terpisah: sentiment_good.csv, sentiment_bad.csv, dan sentiment_neutral.csv.
      ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/2%20aa.png?raw=true)\
      Output Klasifikasi: ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/Output%202%20aa.png?raw=true)
   - Hitung dan simpan jumlah tweets untuk masing-masing kategori sentimen ke dalam file sentiment_counts.csv menggunakan metode summarize_counts().
      ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/2%20b.png?raw=true)

3. Penyimpanan Data
   - Desain skema database dengan tabel yang saling berelasi:
      ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/Soal/3.png?raw=true)
      - tweets (id, text, sentiment_id)
      - sentiments (sentiment_id, sentiment_label)
      - Pastikan sentiment_id di tabel tweets merupakan foreign key yang merujuk ke sentiments.
      ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/3%20a.png?raw=true)
   - Buat class Python DatabaseManager didalam file database_manager.py dengan library SQLAlchemy atau pymysql (jika menggunakan mysql) yang memiliki metode:
      ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/3%20b.png?raw=true)
      - create_tables untuk mendefinisikan dan membuat tabel-tabel di atas jika belum ada.
         ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/3%20b%20(a).png?raw=true)
      - insert_from_csv untuk membaca data dari CSV dan menginsert-nya ke dalam database sesuai tabel yang relevan.
         ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/3%20b%20(b).png?raw=true)\
      Output:
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/Output%203%20bb%20(a).png?raw=true)
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/Output%203%20bb%20(b).png?raw=true)
   - Dokumentasi masing-masing tabel hasil insert dalam bentuk screenshot
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/3%20c%20(a).png?raw=true)
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/3%20c%20(b).png?raw=true)
      - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/Code%20Competence%201%20DE/Screenshot/3%20c%20(c).png?raw=true)

4. Integrasi dengan Google Cloud Storage:
- Buat satu bucket di Google Cloud Storage, dengan nama sentiment_chatgpt_storage, untuk menyimpan semua file yang relevan:
   - sentiment_good.csv
   - sentiment_bad.csv
   - sentiment_neutral.csv
   - sentiment_counts.csv
   - Backup database sentiment_chatgpt.sql
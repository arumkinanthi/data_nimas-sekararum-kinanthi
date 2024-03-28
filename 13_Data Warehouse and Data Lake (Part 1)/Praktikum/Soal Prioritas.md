## Soal Prioritas 1

1. Sebutkan dan jelaskan tantangan yang perlu dihadapi dalam penggunaan Data Warehouse!\
   Jawab:\
   Dalam pengimplementasian data warehouse untuk sistem penyimpanan database, terdapat bebrapa tantangan yang akan dihadapi oleh perusahaan. Kesulitan dalam aspek manajemen struktur data dapat menjadi salah satu tantangan yang akan dihadapi karena jika data yang masuk berjumlah banyak, proses ETL (Extract, Transform, Load) akan memperlambat proses penyimpanan data tersebut ke dalam data warehouse. Sebagai lanjutan dari banyaknya jumlah data yang masuk, sistem penyimpanan akan semakin kesulitan untuk melakukan pencarian data dan analisis dan akan mengurangi kecepatan dan efisiensi. Data warehouse juga membutuhkan cost yang tinggi dengan melibatkan infrastruktur yang cukup kompleks, sumber daya manusia, dan pemrosesan data untuk ETL yang dapat memakan waktu dan biaya besar.
2. Perhatikan diagram ERD berikut.
   Berdasarkan diagram ERD tersebut buatlah berbagai tabel dengan menggunakan Citus.\
   Jawab:
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%201%20Users.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%201%20Categories.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%201%20Posts.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%201%20Comments.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%201.png?raw=true)
   
   

## Soal Prioritas 2

1. Sebuah perusahaan yang bergerak di bidang jasa penyewaan kendaraan bermotor ingin menerapkan penggunaan data warehouse dalam operasional bisnis. Data warehouse nantinya digunakan untuk menganalisis penggunaan kendaraan bermotor, kepuasan konsumen serta menganalisis keuntungan yang diperoleh setiap bulannya. Berdasarkan skenario tersebut buatlah rancangan skema database dalam bentuk diagram ERD. Rancangan dapat dibuat dengan menggunakan aplikasi draw.io atau aplikasi lainnya yang sejenis.\
   Jawab:
   ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/ERD%20Prioritas%202.png?raw=true)


2. Berdasarkan diagram ERD yang sudah dibuat pada nomor 1, buatlah berbagai tabel dengan kriteria sebagai berikut:
   - Menggunakan Citus dalam pembuatan tabel.
   - Menerapkan replication.
   - Menerapkan sharding.\
   Jawab:\
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20a.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20b.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20c.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20d.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20e.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20f.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20g.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20h.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20i.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20j.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20k.png?raw=true)
   - ![alt text](https://github.com/arumkinanthi/data_nimas-sekararum-kinanthi/blob/main/13_Data%20Warehouse%20and%20Data%20Lake%20(Part%201)/Screenshot/Soal%20Prioritas/Prioritas%202%20l.png?raw=true)
   
## Soal Prioritas 1

1. Jelaskan perbedaan antara data terstruktur dan data tidak terstruktur. Berikan contoh untuk masing-masing dan bahas bagaimana mereka biasanya disimpan dan diproses.\
   Jawab: \
   Perbedaan utama antara data terstruktur dan tidak terstruktur ialah data terstruktur adalah data yang disimpan secara tertata ke dalam sebuah tabel data dan mencakup tipe data terpisah seerti angka, teks pendek, dan tanggal. Data tidak terstruktur adalah data tanpa model skema yang ditetapkan.\
   Contoh dari data terstruktur ialah file excel. Data seperti ini umumnya diproses untuk disimpan di sebuah relational database dan dimasukkan ke dalam gudang data/data warehouse yang bersumber dari berbagai resource, seoerti basis data dan sistem transaksi. Data warehouse digunakan untuk menganalisis data dan mengembangkan business intelligence. Proses queri untuk mengolah data terstruktur lebih sederhana karena algoritmanya lebih mudah.\
   Contoh dari data tidak terstruktur ialah kumpulan file video. Data dengan tipe seperti ini memiliki proses pengelolaan yang cepat karena tidak memerlukan format penyimpanan yang ditentukan. Data tidak terstruktur dapat disimpan ke dalam data lake (local maupun cloud) sehingga lebih leluasa.\
   (Sumber: [text](https://aws.amazon.com/compare/the-difference-between-structured-data-and-unstructured-data/))

2. Apa itu basis data relasional dan bagaimana cara kerjanya? Berikan contoh penggunaannya dalam dunia nyata.\
   Jawab: \
   Relational Database/Basis Data Relasional adalah seklompok data dengan relasi yang telah ditentukan sebelumnya di antara data-data tersebut. Relational Database bekerja dengan menyajikan lingkungan sebagai wadah untuk aplikasi agar dapat mengakses data dan menyusunnya kembali tanpa harus mengatur ulang tabel data dari dalam kode aplikasi. Model relasional memformat data ke dalam tabel-tabel (setiap baris mewakili sebuah data dan setiap kolom terdiri dari atribut) untuk kemudan diakses dengan berbagai cara. Contoh penggunaan basis data relasional dalam dunia nyata ialah rekam medis elektronik yang biasanya berisi entitas pasien, diagnosis, obat, hasil lab, rencana perawatan, dan sebagainya. Data rekam medis ini akan saling berkaitan/berelasi antara entitas satu dengan yang lainnya.\
   (Sumber: [text](https://aws.amazon.com/relational-database/))
   
3. Jelaskan konsep normalisasi basis data dan mengapa hal ini penting dalam konteks basis data relasional.\
   Jawab: \
   Normalisasi basis data merupakan proses formatting/pengorganisasian atribut-atribut database untuk mengurangi dan/atau menghilangkan redundansi dan ketergantuangan fungsional sehingga database yang didapatkan memiliki kualitas yang baik dan efisien. Normalisasi database dalam relational database sangat penting untuk dilakukan untuk menghindari redundansi data (data yang sama tetapi berada di tempat yang berbeda) yang akan memakan memori lebih dari yang seharusnya, padahal seharusnya tidak perlu. Normalisasi database juga diperlukan untuk menghilangkan ketergantungan fungsional (weak attributes) serta memastikan bahwa data yang ada di dalam database adalah konsisten dan akurat.\
   (Sumber: [text](https://www.geeksforgeeks.org/introduction-of-database-normalization/))
   
   
## Soal Prioritas 2

Anda diberi tugas untuk merancang sistem basis data untuk sebuah perusahaan e-commerce. Perusahaan ini memiliki data yang sangat beragam, mulai dari data transaksi pelanggan hingga log interaksi pengguna di website. Diskusikan pendekatan yang akan Anda gunakan untuk mengelola data ini, termasuk pemilihan antara basis data relasional dan NoSQL, serta strategi untuk mengintegrasikan data terstruktur dan tidak terstruktur.\
Jawab: \
Perusahaan e-commerce memiliki banyak jenis data, yaitu dapat berupa data transaksi, data customer, data produk, data penjual, data foto/video review produk, dan log interaksi antar pengguna. Untuk data yang testruktur seperti data transaksi, data customer, data produk, data penjual, dapat diproses ke dalam tabel entitas dan disimpan ke dalam database SQL. Sementara untuk data interaksi antar pengguna di website dapat dikategorikan sebagai data tidak terstruktur yang dapat disimpan ke dalam sebuah data lake untuk kemudian diproses saat akan digunakan.\
Untuk melakukan integrasi antara data terstruktur dan tidak testruktur, kita dapat membentuk complete data warehouse. Data tidak terstruktur diubah menjadi data intermediate yang memiliki karakteristik sama dengan data terstruktur dengan teknik *text tagging* dan *annotation* dan hasilnya akan diintegrasikan dengan data terstruktur. Integrasi ini dibantu oleh alat untuk melakukan proses ETL dari database terpisah sehingga kedua sumber data tadi menjadi sebuah storage utuh yaitu Complete Data Warehouse untuk kebutuhan pelaporan dan analisis.\
Sumber: ([text](https://www.researchgate.net/publication/279480483_Integrasi_Data_Terstruktur_dan_Tidak_Terstruktur_dalam_Sistem_Inteligensi_Bisnis))
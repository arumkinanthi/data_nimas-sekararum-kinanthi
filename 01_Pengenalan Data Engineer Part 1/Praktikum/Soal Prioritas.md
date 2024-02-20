## Soal Prioritas 1

1. Sebutkan dan jelaskan berbagai skill yang dibutuhkan untuk menjadi seorang data engineer! (minimal 3)\
   Jawab:
   \
   Beberapa skill yang dibutuhkan untuk menjadi seorang data engineer adalah sebagai berikut [1]:
   - *Data Warehousing* & ETL: Data warehousing merupakan proses penyimpanan data ke dalam data warehouse, sedangkan ETL (*Extract*-*Transform*-*Load*) merupakan proses penggabungan data dari berbagai sumber, penyesuaian format/transformasi data, kemudian penyajian/pemuatan data ke dalam sebuah wadah yang disebut database sehingga skill ini diperlukan oleh data engineer selama proses penyimpanan dan pengarsipan data ke dalam data warehouse/data lake.
   - *Advanced Programming Knowlegde*: Pengetahuan lebih mengenai *programming*, khususnya bahasa pemrograman Python diperlukan oleh data engineer selama melakukan proses ekstrak, transformasi, dan penyimpanan data agar data siap untuk digunakan dan sesuai dengan apa yang diinginkan perusahaan/organisasi.
   - *In-depth knowledge of SQL*/*Database*: SQL (*Structured Query Language*) merupakan bahasa pemrograman yang yang digunakan untuk mengakses, mengolah, maupun memanipulasi data dalam sebuah database sehingga skill SQL/database tentu dibutuhkan untuk menjadi data engineer.
   - *Data architecture* & *pipelining*: Arsitektur data merupakan sebuah ketentuan di dalam organisasi untuk mengatur proses yang dilakukan oleh organisasi tersebut dalam mengumpulkan, mentransformasikan, menyimpan data ke dalam database dan melakukan penyajian data. Sementara pipelining merupakan proses yang ada di dalam data arsitektur, umumnya menggunakan ETL, ELT, Batch, atau Stream pipeline. Kedua skill ini diperlukan oleh data engineer sebagai dasar pemahaman konsep.
   - *Machine Learning concept knowledge*: Pengetahuan mengenai konsep *machine learning* juga dibutuhkan oleh data engineer selama proses mengolah/mentransformasi data sehingga skill ini penting untuk dikuasai.
   - *Scripting*, *reporting* & *data visualization*: *Scripting* merupakan penulisan dan perintah untuk komputer agar menjalankan tugas-tugas tertentu seperti pemrosesan dan pengolahan data, sedangkan *reporting* merupakan penyajian data  seperti melakukan pelaporan yang dapat berguna untuk pengambilan keputusan. Visualisasi data adalah cara yang digunakan untuk menyajikan data seperti grafik dan diagram yang merepresentasikan data dan informasi yang sudah diolah sebelumnya agar dapat dimengerti oleh perusahaan/organisasi.\
   
2. Sebutkan dan jelaskan urgensi/pentingnya peran data engineer dalam industri di saat ini!\
   Jawab:
   \
   Dunia industri saat ini sudah memasuki Revolusi Industri 4.0, yang ditandai oleh kemajuan pesat teknologi internet, menunjukkan bahwa big data akan menjadi aset yang sangat berharga di masa mendatang. Pada era ini, kehadiran big data akan menjadi kunci untuk meraih keunggulan dalam persaingan di berbagai sektor industri. Dengan kapasitasnya dalam menyediakan informasi yang penting, big data akan memainkan peran utama dalam memberikan organisasi kemampuan untuk membuat keputusan yang cerdas dan didasarkan pada data yang akurat. Ini akan membantu mereka mengatasi berbagai tantangan yang kompleks yang dihadapi di era revolusi industri 4.0 [2]. Di sinilah peran data engineer sebagai penyedia data, mulai dari mengumpulkan, melakukan penyesuaian format, dan penyajian data sehingga data-data tersebut siap dan dapat digunakan oleh data scientist dan data analyst nantinya. Oleh karena hal-hal tersebut, dapat disimpulkan bahwa peran data engineer sangat penting dan mendesak dalam industri saat ini.

   [1] Sawitri, D. 2019. Revolusi Industri 4.0: Big Data Menjawab Tantangan Revolusi Industri 4.0. Jurnal Ilmiah Maksitek, 4(3), pp. 1-9.\
   [2] Syamsu, M., & Widodo. 2021. Peran Data Science dan Data ScientistUntuk Mentransformasi Data Dalam Industri 4.0. Jurnal Teknologi Informasi (JUTECH), 2(1) pp. 27-36.\
   
   
## Soal Prioritas 2
1. Sebuah rumah sakit bernama Alta Medika ingin mengelola berbagai data yang telah dikumpulkan seperti data pasien, data komplain, data survei kepuasan pelayanan, data dokter dan data lainnya. Untuk mengelola berbagai data tersebut dapat dilakukan dengan mengembangkan sebuah data pipeline. Berdasarkan kasus ini sebutkan jenis data pipeline yang cocok digunakan beserta alasannya!
   \
   Jawab:
   \
   Data pipeline dapat dibagi berdasarkan urutan proses transformasinya (ETL dan ELT) dan berdasarkan sumber datanya (Batch dan Stream). Pada contoh kasus di atas, dapat diketahui bahwa sumber data yang digunakan berasal dari banyak sumber seperti data pasien, data komplain, data survei kepuasan pelayanan, data dokter dan data lainnya. Selain itu, rumah sakit biasanya membutuhkan hasil dari data yang sudah diproses tersebut secara langsung dan berkelanjutan.\
   Berdasarkan sumber data tersebut, dapat ditentukan bahwa jenis data pipeline yang cocok digunakan oleh Rumah Sakit Alta Medika menurut sumber datanya adalah Stream Pipeline karena sumber data dikumpulkan secara kontinu dan hasil transformasi data dapat dihasilkan secara real-time serta terus berlanjut mengikuti arus data mentah yang masuk. Kemudian untuk jenis data pipeline yang cocok digunakan menurut proses transformasinya adalah ETL (Extract-Transform-Load) karena proses ini mengambil dan menggunakan data dari berbagai sumber untuk dilakukan transformasi secara bersamaan.\
   Kemudian, data-data yang telah diproses tersebut dapat langsung ditampilkan pada aplikasi yang digunakan secara real-time maupun disimpan ke dalam data warehouse yang biasanya digunakan untuk data yang telah melalui proses transformasi terlebih dahulu sehingga data lebih terstruktur.
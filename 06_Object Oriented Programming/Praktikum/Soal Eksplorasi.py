"""
Desain Sistem Pemesanan:
- Tambahkan metode pesanKelas() dan batalkanKelas() di kelas KelasLatihan.
- Override metode tersebut di kelas Yoga dan AngkatBeban dengan aturan pemesanan dan pembatalan khusus.
Implementasi dan Demonstrasi:
- Buat sistem yang memungkinkan pelanggan untuk memesan dan membatalkan kelas.
- Demonstrasi kasus pemesanan dan pembatalan untuk Yoga dan AngkatBeban, menunjukkan bagaimana polimorfisme digunakan dalam kasus ini.
"""

class Pelanggan:
   
   def __init__(self, nama, usia, idPelanggan):
      self.__nama = nama
      self.__usia = usia
      self.__idPelanggan = idPelanggan
      self.__daftarkelas = []
      
   def getNama(self):
      return self.__nama
   
   def setNama(self, nama):
      self.__nama = nama
   
   def getUsia(self):
      return self.__usia
   
   def setUsia(self, usia):
      self.__usia = usia
   
   def getIdPelanggan(self):
      return self.__idPelanggan
   
   def setIdPelanggan(self, idPelanggan):
      self.__idPelanggan = idPelanggan
      
   def getDaftarKelas(self):
      return self.__daftarkelas
     
   def setDaftarKelas(self, kelas):
      self.__daftarkelas.append(kelas)
      
   def tampilkanInfo(self):
      print(f"\nID Pelanggan\t: {self.getIdPelanggan()}")
      print(f"Nama Pelanggan\t: {self.getNama()}")
      print(f"Usia\t\t: {self.getUsia()} tahun")
      
class Pelatih:
   
   def __init__(self, nama, spesialisasi, tahunPengalaman):
      self.__nama = nama
      self.__spesialisasi = spesialisasi
      self.__tahunPengalaman = tahunPengalaman
   
   def getNama(self):
      return self.__nama
   
   def setNama(self, nama):
      self.__nama = nama
   
   def getSpesialisasi(self):
      return self.__spesialisasi
   
   def setSpesialisasi(self, spesialisasi):
      self.__spesialisasi = spesialisasi
   
   def getTahunPengalaman(self):
      return self.__tahunPengalaman
   
   def setTahunPengalaman(self, tahunPengalaman):
      self.__tahunPengalaman = tahunPengalaman
      
   def tampilkanInfo(self):
      print(f"\nNama Pelatih\t: {self.getNama()}")
      print(f"Spesialisasi\t: {self.getSpesialisasi()}")
      print(f"Total Pengalaman: {self.getTahunPengalaman()} tahun")

class KelasLatihan(Pelatih):
   
   def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal):
      super().__init__(nama, spesialisasi, tahunPengalaman)
      self.__jenisLatihan = jenisLatihan
      self.__jadwal = jadwal
      
   def getJenisLatihan(self):
      return self.__jenisLatihan
   
   def setJenisLatihan(self, jenisLatihan):
      self.__jenisLatihan = jenisLatihan
   
   def getJadwal(self):
      return self.__jadwal
   
   def setJadwal(self, jadwal):
      self.__jadwal = jadwal
      
   def pesanKelas(self, object = Pelanggan):
      pass
   
   def batalkanKelas(self, object = Pelanggan):
      pass
   
   def tampilkanInfo(self):
      super().tampilkanInfo()
      print(f"Jenis Latihan\t: {self.getJenisLatihan()}")
      print(f"Jadwal\t\t: Hari {self.getJadwal()}")
      
class Yoga(KelasLatihan):
   
   def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal, tingkatKesulitan, posisiYoga):
      super().__init__(nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal)
      self.__tingkatKesulitan = tingkatKesulitan
      self.__posisiYoga = posisiYoga
   
   def getTingkatKesulitan(self):
      return self.__tingkatKesulitan
   
   def setTingkatKesulitan(self, tingkatKesulitan):
      self.__tingkatKesulitan = tingkatKesulitan
   
   def getPosisiYoga(self):
      return self.__posisiYoga
   
   def setPosisiYoga(self, posisiYoga):
      self.__posisiYoga = posisiYoga
   
   def pesanKelas(self, object = Pelanggan):
      super().pesanKelas(object)
      state = False
      for i in object.getDaftarKelas():
         if i == self:
            state = True
      if state == False:
         object.setDaftarKelas(self)
         print(f"\nAnda telah memesan kelas pelatih {self.getNama()} dengan jenis latihan {self.getJenisLatihan()}")
      else: 
         print("\nAnda tidak bisa memesan kembali kelas ini!")
      print("\nDaftar kelas Anda setelah proses pemesanan:")
      for i in object.getDaftarKelas():
         i.tampilkanInfo()
         
   def batalkanKelas(self, object = Pelanggan):
      super().batalkanKelas(object)
      count = 0
      list = object.getDaftarKelas()
      for i in object.getDaftarKelas():
         if ClassType(i) == "Yoga":
            count += 1
      if count == 1:
         print(f"\nKelas coach {self.getNama()} dengan jenis latihan {self.getJenisLatihan()} tidak dapat dibatalkan karena harus terdapat minimal 1 kelas Yoga.")
      else: 
         list.remove(self)
         print(f"\nAnda telah membatalkan kelas pelatih {self.getNama()} dengan jenis latihan {self.getJenisLatihan()}")
      print("\nDaftar Kelas Anda setelah proses pembatalan:")
      for i in object.getDaftarKelas():
         i.tampilkanInfo()
   
   def tampilkanInfo(self):
      super().tampilkanInfo()
      print("Nama Posisi Yoga:", self.getPosisiYoga())
      print("Tingkat Kesulitan :", self.getTingkatKesulitan())

class AngkatBeban(KelasLatihan):
   
   def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal, berat):
      super().__init__(nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal)
      self.__beratMaksimum = 20
      self.__berat = berat
      
   def getBeratMaksimum(self):
      return self.__beratMaksimum
   
   def getBerat(self):
      return self.__berat
   
   def setBerat(self, berat):
      self.__berat = berat
   
   def pesanKelas(self, object = Pelanggan):
      super().pesanKelas(object)
      state = False
      for i in object.getDaftarKelas():
         if i.getNama() == self.getNama():
            state = True
      if state == False:
         object.setDaftarKelas(self)
      else: 
         print(f"Anda tidak dapat memesan kembali kelas pelatih {self.getNama()}!")
      print("\nDaftar kelas Anda setelah proses pemesanan:")
      for i in object.getDaftarKelas():
         i.tampilkanInfo()
   
   def batalkanKelas(self, object = Pelanggan):
      super().batalkanKelas(object)
      list = object.getDaftarKelas()
      list.remove(self)
      print("\nDaftar Kelas Anda setelah proses pembatalan:")
      for i in list:
         i.tampilkanInfo()
   
   def tampilkanInfo(self):
      super().tampilkanInfo()
      print(f"Berat Maksimum\t: {self.getBeratMaksimum()} kg")
      print(f"Berat Beban yang dipilih : {self.getBerat()} kg")

def ClassType(object):
   if isinstance(object, Yoga):
      return "Yoga"
   else:
      pass

pelanggan1 = Pelanggan("Lanang", 25, "P01")

kelasYoga1 = Yoga("Liza", "Yoga", 10, "Meditasi", "Sabtu", "Easy", "Mountain Pose")
kelasYoga2 = Yoga("Liza", "Yoga", 10, "Kekuatan", "Minggu", "Hard", "Plank Pose")
kelasYoga1.pesanKelas(pelanggan1) # memesan kelas Yoga 1
kelasYoga1.pesanKelas(pelanggan1) # mencoba memesan kembali kelas Yoga 1
kelasYoga2.pesanKelas(pelanggan1) # memesan kelas Yoga 2
kelasYoga1.batalkanKelas(pelanggan1) # membatalkan kelas Yoga 1
kelasYoga2.batalkanKelas(pelanggan1) # membatalkan kelas Yoga 2
kelasAngkatBeban1 = AngkatBeban("Ardi", "Angkat Beban", 15, "Lower Body", "Minggu", 0)
kelasAngkatBeban2 = AngkatBeban("Rafi", "Angkat Beban", 15, "Upper Body", "Minggu", 0)
kelasAngkatBeban1.pesanKelas(pelanggan1) # memesan kelas Angkat Beban 1
kelasAngkatBeban1.pesanKelas(pelanggan1) # mencoba memesan kembali kelas Angkat Beban 1
kelasAngkatBeban2.pesanKelas(pelanggan1) # memesan kelas Angkat Beban 2
kelasAngkatBeban1.batalkanKelas(pelanggan1) # membatalkan kelas Angkat Beban 1
kelasAngkatBeban2.batalkanKelas(pelanggan1) # membatalkan kelas Angkat Beban 2



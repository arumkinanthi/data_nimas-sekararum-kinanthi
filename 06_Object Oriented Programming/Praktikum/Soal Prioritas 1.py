# Soal Prioritas 1: Sistem untuk mengelola aktivitas di sebuah pusat kebugaran, termasuk pelanggan, pelatih, dan berbagai kelas latihan.

class Pelanggan:
   
   def __init__(self, nama, usia, idPelanggan):
      self.__nama = nama
      self.__usia = usia
      self.__idPelanggan = idPelanggan
      
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
   
   def tampilkanInfo(self):
      super().tampilkanInfo()
      print(f"Jenis Latihan\t: {self.getJenisLatihan()}")
      print(f"Jadwal\t\t: Hari {self.getJadwal()}")
      
pelanggan = Pelanggan("Fajar", 20, "P01")
pelatih1 = Pelatih("Rafi", "Sepak Bola", 10)
pelatih2 = Pelatih("Liza", "Basket", 7)
kelasLatihan1 = KelasLatihan("Rafi", "Sepak Bola", 10, "Sprint Bukit", "Senin")
kelasLatihan1 = KelasLatihan("Rafi", "Sepak Bola", 10, "Squat Jump", "Selasa")
kelasLatihan2 = KelasLatihan("Rafi", "Sepak Bola", 10, "Latihan Koordinasi", "Sabtu")
kelasLatihan3 = KelasLatihan("Liza", "Basket", 7, "Upper Body", "Rabu")
kelasLatihan4 = KelasLatihan("Liza", "Basket", 7, "Lower Body", "Minggu")

pelanggan.tampilkanInfo()
pelatih1.tampilkanInfo()
pelatih2.tampilkanInfo()
kelasLatihan1.tampilkanInfo()
kelasLatihan2.tampilkanInfo()
kelasLatihan3.tampilkanInfo()
kelasLatihan4.tampilkanInfo()

# Soal Prioritas 2: Memperluas sistem manajemen pusat kebugaran dengan menambahkan fitur khusus untuk berbagai jenis kelas latihan, seperti Yoga dan Angkat Beban, dengan fokus pada detail lanjutan dari inheritance dan polymorphism.

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
   
   def aturPosisiYoga(self):
      print("\nBerikut pilihan posisi Yoga:")
      print("1. Mountain Pose\n2. Chair Pose\n3. Triangle Pose\n4. Bridge Pose\n5. Plank Pose")
      pilihan = int(input("Masukkan posisi Yoga yang anda inginkan! (masukkan angkanya saja, misalnya: '1' atau '2'): "))
      if 0 < pilihan <= 5:
         if pilihan == 1:
            self.setPosisiYoga("Mountain Pose")
            self.setTingkatKesulitan("Easy")
         elif pilihan == 2:
            self.setPosisiYoga("Chair Pose")
            self.setTingkatKesulitan("Easy")
         elif pilihan == 3:
            self.setPosisiYoga("Triangle Pose")
            self.setTingkatKesulitan("Medium")
         elif pilihan == 4:
            self.setPosisiYoga("Bridge Pose")
            self.setTingkatKesulitan("Hard")
         elif pilihan == 5:
            self.setPosisiYoga("Plank Pose")
            self.setTingkatKesulitan("Hard")
         print(f"Anda memilih posisi yoga {self.getPosisiYoga()} yang memiliki tingkat kesulitan {self.getTingkatKesulitan()}.")
         self.tampilkanInfo()
      else:
         print("Pilihan Anda tidak sesuai! Silakan memilih kembali.")
         self.aturPosisiYoga()
   
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
   
   # def setBeratMaksimum(self):
   #    self.__beratMaksimum = 20
   
   def getBerat(self):
      return self.__berat
   
   def setBerat(self, berat):
      self.__berat = berat
   
   def aturBeratBeban(self):
      print("\nBerat beban tidak boleh sama dengan '0' atau melebihi batas maksimum berat beban, yaitu 20 kg.")
      berat = int(input("Silakan masukkan berat beban yang Anda inginkan! (masukkan angkanya saja, misalnya: '5' atau '10'): "))
      if 0 < berat <= self.getBeratMaksimum():
         self.setBerat(berat)
         print(f"Anda memilih beban seberat {self.getBerat()} kg.")
         self.tampilkanInfo()
      elif berat > self.getBeratMaksimum():
         print("Berat yang Anda masukkan melebihi batas berat maksimum yang diizinkan! Silakan masukkan kembali berat yang diinginkan.")
         self.aturBeratBeban()
      else:
         print("Pilihan Anda tidak sesuai! Silakan memilih kembali.")
         self.aturBeratBeban()
   
   def tampilkanInfo(self):
      super().tampilkanInfo()
      print(f"Berat Maksimum\t: {self.getBeratMaksimum()} kg")
      print(f"Berat Beban yang dipilih : {self.getBerat()} kg")
 
      
def ClassType(object):
   if isinstance(object, Yoga):
      object.aturPosisiYoga()
   elif isinstance(object, AngkatBeban):
      object.aturBeratBeban()
   elif isinstance(object, KelasLatihan):
      object.tampilkanInfo()
   else:
      pass
   

kelasYoga = Yoga("Kinan", "Yoga", 10, "Meditasi", "Sabtu", None, None)
ClassType(kelasYoga)
kelasAngkatBeban = AngkatBeban("Ardi", "Angkat Beban", 15, "Lower Body", "Minggu", 0)
ClassType(kelasAngkatBeban)
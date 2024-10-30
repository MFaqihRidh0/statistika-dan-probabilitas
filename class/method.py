class Mahasiswa ():
    nama = 'name'
    #method
    def belajar(self):
        print(self.nama, 'belajar mandiri')

faqih =  Mahasiswa()
ucup = Mahasiswa ()

faqih.nama = "muhammad faqih ridho"
ucup.nama  = "ucup surucup"

#contoh yang SALAH print (faqih.belajar)
#contoh yang benar
faqih.belajar()
ucup.belajar()
class item:
    #class atributes
    Discount = 0.8 
    #method
    def __init__ (self, name :str , harga : float, kuantitas=0):
        #assert (penegasan) bisa digunakan agar harga dan kuantitas > 0
        assert harga >= 0 , f"harga {harga} harus lebih besar dari 0" #format string
        assert kuantitas >= 0, f"harga {kuantitas} harus lebih besar dari 0"

        self.name = name
        self.harga =harga
        self.kuantitas = kuantitas
    def calculator (self):
        return self.harga*self.kuantitas
    def apply_discount(self):
        #self.harga = self.harga*item.Discount #untuk mengkases discount harus menyebut class nya dulu
        self.harga = self.harga*self.Discount #bagus untuk membuat menjadi instance level sehingga instance bisa menyesuaikan mau diskon berapa
#instances
item1 = item("HandPhone", 100,3 )
item2 = item("laptop", 100,3)

#panggil method karena dalam method tidak menetapkan pembayaran tertentu
#maka item 1 mengakses pada class level
item1.apply_discount()
#print hasil method apply discount
print (item1.harga)

#karena discount di spesifikkan maka item 2 mengakses pada instance level
item2.Discount =0.7 #inisialisasi diskonnya berapa dulu baru memanggil method apply diskonnya agar masuk perhitungan di methodnya
item2.apply_discount()
print (item2.harga)
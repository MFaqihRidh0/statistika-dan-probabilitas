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
        self.harga = self.harga*item.Discount #untuk mengkases discount harus menyebut class nya dulu
#instances
item1 = item("HandPhone", 100,3 )
item2 = item("laptop", 500,5)

print (item1.calculator())
print (item2.calculator())
#ketika item 1 tidak menemukan tidak bisa menemukan discount pada method nya dia akan mencari di class item
#karena di class item ada atribute discount maka itu diakses
print (item1.Discount)

print  (item.__dict__) # melihat seluruh atribut pada level class
print (item1.__dict__) #melihat seluruh atribut pada lavel instances
#panggil method 
item1.apply_discount()
#print hasil method apply discount
print (item1.apply_discount)
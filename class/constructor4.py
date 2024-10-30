class item:
    #class atributes
    Discount = 0.8 
    All =[]
    #method
    def __init__ (self, name :str , harga : float, kuantitas=0):
        #assert (penegasan) bisa digunakan agar harga dan kuantitas > 0
        assert harga >= 0 , f"harga {harga} harus lebih besar dari 0" #format string
        assert kuantitas >= 0, f"harga {kuantitas} harus lebih besar dari 0"

        self.name = name
        self.harga =harga
        self.kuantitas = kuantitas
        #menambahkan instances ke variabel All array
        item.All.append(self)
    def calculator (self):
        return self.harga*self.kuantitas
    def apply_discount(self):
        self.harga = self.harga*item.Discount
    #__repr__ adalah method untuk merepresentasikan ke display, kita dapat mengontrol apa yang ada didisplay
    def __repr__(self):
        return f"item ('{self.name}', {self.harga}, {self.kuantitas})"
    
item1 = item("HandPhone", 100,3 )
item3 = item("mouse", 500,5)
item4 = item("HandPhone", 100,3 )
item5 = item("cas laptop", 400,5)
item6 = item("meja", 700,3 )

print (item.All)
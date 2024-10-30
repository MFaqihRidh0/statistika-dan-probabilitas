import csv
class Item:
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
        Item.All.append(self)
    def calculator (self):
        return self.harga*self.kuantitas
    def apply_discount(self):
        self.harga = self.harga*Item.Discount
    
    #decoration di python untuk mengganti behaviour dari method
    @classmethod
    def instantiate_from_csv (cls): #menggunakan cls untuk menginstantiate class dri method dan tidak menggunakan self agar tidak bingung
        with open('CommaSeparatedValue/items.csv', 'r') as f : # 'r' untuk hanya membaca file yang ada di csv
            reader =csv.DictReader(f) #read content as list for library
            items = list(reader) #convert reader menajdi list
            
            for item in items :
                cls(
                    name=item.get('name'),
                    harga=float(item.get('harga')),
                    kuantitas=int(item.get('kuantitas')),
                )
    def __repr__(self):
        return f"item ('{self.name}', {self.harga}, {self.kuantitas})"
    
Item.instantiate_from_csv()
print (Item.All)
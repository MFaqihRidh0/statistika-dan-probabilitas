class item:
    #ketika function didalam class disebut method seperti dibawah ini
    #parameter self digunakan agar method dapat digunakan oleh instances
    def calculate_total_price (self, x, y):
        return x*y
item1 = item()
item1.name = "phone"
item1.harga = 10000
item1.jumlah = 5
print (item1.calculate_total_price (item1.harga, item1.jumlah))

item2 =item()
item2.name = "laptp"
item2.harga = 50000
item2.jumlah = 3
print (item2.calculate_total_price (item2.harga, item2.jumlah))

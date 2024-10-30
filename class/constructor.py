class item:
    def __init__ (self, name, harga, kuantitas):
        self.name = name
        self.harga =harga
        self.kuantitas = kuantitas
#instances
item1 = item("HandPhone", 100 , 5)
item2 = item("laptop", 500, 3)

print(item1.name)
print(item1.harga)
print(item1.kuantitas)
print(item2.name)
print(item2.harga)
print(item2.kuantitas)
from abc import ABC, abstractmethod

# Kelas abstrak Animal
class Animal(ABC):
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @abstractmethod
    def make_sound(self) -> str:
        pass

# Kelas konkret Cat yang diturunkan dari Animal
class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"

# Kelas konkret Dog yang diturunkan dari Animal
class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"

# Kelas AnimalParade
class AnimalParade:
    def __init__(self):
        self._list_animals = []

    def add_animal(self, animal: Animal):
        self._list_animals.append(animal)

    def start_parade(self, rounds: int):
        for _ in range(rounds):
            for animal in self._list_animals:
                print(f"{animal.name} makes sound: {animal.make_sound()}")

# Fungsi untuk membaca input dan menjalankan parade
def main():
    n = int(input("Enter the number of animals: "))  # Input jumlah hewan
    parade = AnimalParade()
    
    for _ in range(n):
        animal_info = input().split()  # Input jenis hewan dan nama
        animal_type = animal_info[0]
        animal_name = animal_info[1]
        
        if animal_type == "Cat":
            parade.add_animal(Cat(animal_name))
        elif animal_type == "Dog":
            parade.add_animal(Dog(animal_name))
    
    rounds = int(input("Enter the number of rounds: "))  # Input jumlah putaran
    parade.start_parade(rounds)  # Memulai parade

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
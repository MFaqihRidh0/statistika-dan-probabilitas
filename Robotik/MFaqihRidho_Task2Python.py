from abc import ABC, abstractmethod
from typing import List

# Kelas abstrak Instrument
class Instrument(ABC):
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def play(self) -> str:
        pass

class Guitar(Instrument):
    def play(self) -> str:
        return "Strum Strum"


class Piano(Instrument):
    def play(self) -> str:
        return "Ting Ting"


class MusicStudio:
    def __init__(self):
        self._list_instruments: List[Instrument] = []

    def add_instrument(self, instrument: Instrument):
        self._list_instruments.append(instrument)

    def play_instruments(self):
        for instrument in self._list_instruments:
            print(f"{instrument.name} makes sound: {instrument.play()}")


def main():
    n = int(input("Enter the number of instruments: "))  
    studio = MusicStudio()
    
    for _ in range(n):
        instrument_info = input().split()  
        instrument_type = instrument_info[0]
        instrument_name = instrument_info[1]
        
        if instrument_type == "Guitar":
            studio.add_instrument(Guitar(instrument_name))
        elif instrument_type == "Piano":
            studio.add_instrument(Piano(instrument_name))
    
    studio.play_instruments()  

if __name__ == "__main__":
    main()
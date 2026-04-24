from typing import List


# Завдання 1
class Passenger:
    def __init__(self, name:str, destination:str):
        self._name = name
        self._destination = destination

# Завдання 2
class Transport:
    def __init__(self, speed:int):
        self._speed = speed

    def move(self,destination:str, distance:int):
        traveltime = (distance/self._speed) * 60
        print(f'you arrived at {destination} with {traveltime} minutes')

# Завдання 3
class Bus(Transport):
    def __init__(self ,speed:int, passengers:List[Passenger], capacity:int):
        super().__init__(speed)

        self._passengers = passengers
        self._capacity = capacity

    def board_passenger(self, passenger:Passenger):
        if len(self._passengers) < self._capacity:
            self._passengers.append(passenger)
        else:
            print(f'The bus is full. Wait for next')

    def move(self, destination:str, distance:int):
        quit = 0
        for passenger in self._passengers:
            if passenger._destination == destination:
                self._passengers.remove(passenger)
                quit += 1

        print(f'you arrived at {destination} and quit {quit} passengers')

        super().move(destination, distance)

p1 = Passenger("Alice", "Baku")
p2 = Passenger("Bob", "Sumqayit")
p3 = Passenger("Charlie", "Baku")

bus = Bus(speed=60, passengers=[p1, p2, p3], capacity=5)

bus.move("Baku", 30)

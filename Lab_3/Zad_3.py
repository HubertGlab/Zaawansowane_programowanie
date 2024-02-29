class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'wymiary: {self.area}, liczba pokoi: {self.rooms}, cena: {self.price}, adres: {self.address}'


class House(Property):
    def __init__(self, plot: int, area, rooms: int, price, address):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'wymiary: {self.area}, liczba pokoi: {self.rooms}, cena: {self.price}, adres: {self.address}, działka:'\
               f'rozmiar działki: {self.plot}'


class Flat(Property):
    def __init__(self, floor, area, rooms: int, price, address):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'wymiary: {self.area}, liczba pokoi: {self.rooms}, cena: {self.price}, adres: {self.address}, działka:'\
               f'liczba pięter: {self.floor}'


house = House(1000, '60x40', 7, 20000, 'Juana 103')
flat = Flat(2, '20x30', 4, 10000, 'Dzulsa 200')

print(house)
print(flat)
class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def place (self, mass, strong):
        road_mass = self.length * self.width * mass * strong
        print(road_mass)

length = int(input("Введите дину дороги "))
width = int(input("Введите ширину дороги "))
road = Road(length, width)
road.place(25, 5)

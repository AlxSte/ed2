class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            return print(f"машина уже движется со скоростью {self.speed}")
        else:
            self.speed += 1
            return print(f"машина начала движение, скорость {self.speed}")

    def stop(self):
        if self.speed == 0:
            return print(f"машина уже стоит")
        else:
            self.speed = 0
            return print(f"машина остановлена")

    def turn(self):
        turn = input("1: налево, 2: направо, 3: развернуться: ")
        if turn == '1':
            return print("машина повернула налево")
        elif turn == '2':
            return print("машина повернула направо")
        elif turn == '3':
            return print("машина развернулась")
        else:
            return print("неверное значение")

    def show_speed(self):
        return print(f"скорость: {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f"скорость привышена {self.speed}")
        else:
            return print(f"скорость {self.speed}")

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f"скорость привышена {self.speed}")
        else:
            return print(f"скорость {self.speed}")
class SportCar(Car):
    pass
class PoliceCar(Car):
    pass

car = Car(60, "красная", "маша", False)
car.go()
car.stop()
car.turn()
car.show_speed()

car = TownCar(61, "красная", "маша", False)
#car.go()
#car.stop()
#car.turn()
car.show_speed()
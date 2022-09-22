class Wokrker:

    def __init__(self, name, surname, position, income):
     self.name = name
     self.surname =surname
     self.position = position
     self._income = income

class Position(Wokrker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


pos = Position(name='polina',
               surname='polinova',
               position='admin',
               income={"wage": 100, "bonus": 50})

pos.get_full_name()
pos.get_total_income()



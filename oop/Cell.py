class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(self.amount)

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        if self.amount > other.amount:
            return self.amount - other.amount
        else:
            return f'Неверные данные'

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(round(self.amount / other.amount))

    def make_orde(self, rows):
        numbs = "\n".join("*" * rows for el in range(self.amount // rows))
        return f'{numbs}\n{"*" * (self.amount % rows)}'

cell1 = Cell(24)
cell2 = Cell(5)

print(cell1.make_orde(5))
print(cell1)
cell3 = cell1 / cell2
print(cell3)




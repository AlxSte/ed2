from abc import ABC, abstractclassmethod

class Clothes(ABC):
    @staticmethod
    def count_total(clothes_list):
        return sum(sh.cloth for sh in clothes_list)

    @property
    @abstractclassmethod
    def cloth(self):
        pass

    def __add__(self, other):
         return self.cloth + other.cloth

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def cloth(self):
        print(f'{round((self.size/6.5)+0.5)}')
        return round((self.size/6.5)+0.5)

class Costume(Clothes):
    def __init__(self, hight):
        self.hight = hight

    @property
    def cloth(self):
        print(f'{round(2 * self.hight + 0.3)}')
        return round(2 * self.hight + 0.3)

coat = Coat(300)
costume = Costume(200)
clothes_ls = [coat, costume]
print(Clothes.count_total(clothes_ls))
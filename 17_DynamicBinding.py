"""
В унаследованном классе SpecialDict() переопределяется магический метод __len__, который возвращает заранее заданное значение.
В родительском классе UsualDict() метод __len__ работает стандартным образом.
"""

class UsualDict():
    def __init__(self):
        self.inner_dict = {1,2,3}

    def __len__(self):
        return len(self.inner_dict)


class SpecialDict(UsualDict):
    def __len__(self):
        return 10

b = UsualDict()
c = SpecialDict()
print(len(b))   # 3
print(len(c))   # 10
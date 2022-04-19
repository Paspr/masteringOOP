# случай 1. метод публичен в родительском классе А и публичен в его потомке B

class Parent():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    pass

c = Child()
print(c.get_value()) # 5


"""
случаи 2 и 3 не нашел, как сделать
2. метод публичен в родительском классе А и скрыт в его потомке B
3. метод скрыт в родительском классе А и публичен в его потомке B
"""


# случай 4. метод скрыт в родительском классе А и скрыт в его потомке B
class Parent2():
    def __init__(self):
        self.value = 5

    def __get_value(self):
        return self.value

class Child2(Parent2):
    pass

c = Child2()
print(c.__get_value()) # AttributeError: 'Child' object has no attribute '__get_value'

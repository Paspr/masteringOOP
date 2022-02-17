import random, math

# inheritance and polymorphism example
# Square adn Circle classes are inherited from Polygon base class
# all classes have calculate_area method which is calculated differently depending on the class

class Polygon():
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        print(f"{self.name} doesn't have area")

class Square(Polygon):
    def __init__(self, name):
      self.width = random.randint(10, 20)
      self.height = random.randint(10, 20)
      super().__init__(name)

    def calculate_area(self):
        print(f"{self.name} area is {str(self.width * self.height)}")

class Circle(Polygon):
    def __init__(self, name):
      self.radius = random.randint(10, 20)
      super().__init__(name)

    def calculate_area(self):
        print(f"{self.name} area is {str(self.radius * math.pi * math.pi)}")


polygon = Polygon('Generic polygon')
square = Square('Square')
circle = Circle('Circle')

figures_list = [polygon, square, circle]

for figure in figures_list:
    figure.calculate_area()


# composition example
# MainMenu class contains methods of ViewMenu and SendMenu classes

class ViewMenu():
    def view_file(self):
        print("Viewing a file...")

class SendMenu():
    def send_file(self):
        print("Sending a file...")

class MainMenu():
    def __init__(self, name):
        self.name = name
        self.v = ViewMenu()
        self.s = SendMenu()
    
    def view(self):
        return self.v.view_file()
    
    def send(self):
        return self.s.send_file()

example_menu = MainMenu('Main menu object')
example_menu.send()
example_menu.view()
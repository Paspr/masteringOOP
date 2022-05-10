# пример полиморфного метода

class classA:
  def write(self):
    print("classA is here")

class classB:
  def write(self):
    print("classB is here")

# полиморфный метод
def write_on_screen(obj):
  obj.write()

objA = classA()
objB = classB()

write_on_screen(objA) # classA is here
write_on_screen(objB) # classB is here


# пример ковариантного метода
# взят с https://blog.magrathealabs.com/pythons-covariance-and-contravariance-b422c63f57ac

from typing import TypeVar, Generic, Iterable, Iterator

List_co = TypeVar('List_co', covariant=True)

class ImmutableList(Generic[List_co]):
    
    def __init__(self, items: Iterable[List_co]) -> None:
        pass
    
    def __iter__(self) -> Iterator[List_co]:
        pass
    
class Employee():
    pass

class Manager(Employee):
    pass

# ковариантный метод
def list_employees(employees: ImmutableList[Employee]) -> None:
    for employee in employees:
        print(employee)

managers = ImmutableList[Manager()]

list_employees(managers)
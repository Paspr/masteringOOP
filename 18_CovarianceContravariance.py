# ковариантность и контравариантность можно показать с помощью MyPy

# пример для ковариантности
# взят с
# https://blog.daftcode.pl/covariance-contravariance-and-invariance-the-ultimate-python-guide-8fabc0c24278
from typing import Tuple, Callable

class Animal: ...
class Dog(Animal): ...

an_animal: Animal = Animal()
lassie: Dog = Dog()
snoopy: Dog = Dog()

animals: Tuple[Animal, ...] = (an_animal, lassie)
dogs: Tuple[Dog, ...] = (lassie, snoopy)

#dogs = animals # ошибка MyPy, animals может содержать других животных, не только собак
animals = dogs # правильное присвоение, все собаки являются animals


# пример контравариантности
# взят с
# https://rednafi.github.io/reflections/variance-of-generic-types-in-python.html

def factory(func: Callable[[float], None]) -> Callable[[float], None]:
    return func


def foo(number: int) -> None:
    pass

def bar(number: float) -> None:
    pass

#factory(foo) # ошибка MyPy
factory(bar)  # правильный вызов

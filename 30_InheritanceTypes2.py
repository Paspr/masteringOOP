# Наследования вариаций

# Наследование с функциональной вариацией

class PlusCalc:
    def operation_exec(self, a, b):
        print(a + b)

class MulCalc(PlusCalc):
    def operation_exec(self, a, b):
        print(a * b)

# Наследование с вариацией типа

class TwoAdder:
    def add(self, a, b):
        result = a + b
        print(result)

class ThreeAdder(TwoAdder):
    def add(self, a, b, c):
        result = a + b + c
        print(result)


# Наследование с конкретизацией

class GenericParser:
    def upload_file(self):
        pass

    def extract_content(self):
        pass

class ParserXLS(GenericParser):
    def upload_file(self):
        print("XLS file is uploaded")
    
    def extract_content(self):
        print("XLS content is found")

class ParserPDF(GenericParser):
    def upload_file(self):
        print("PDF file is uploaded")
    
    def extract_content(self):
        print("PDF content is found")

genericExample = GenericParser()
genericExample.extract_content() # no output
genericExample.upload_file()  # no output

XLSExample = ParserXLS()
XLSExample.extract_content() # XLS file is uploaded
XLSExample.upload_file() # XLS content is found

PDFExample = ParserPDF()
PDFExample.extract_content() # PDF file is uploaded
PDFExample.upload_file() # PDF content is found


# Структурное наследование

class Vehicle():
    pass

class Flying():
    def __init__(self):
        print("Flying")

class FlyingCar(Vehicle, Flying):
    def __init__(self):
        super().__init__()
        print("Car")

class FlyingBike(Vehicle, Flying):
    def __init__(self):
        super().__init__()
        print("Bike")

test_car = FlyingCar() # Flying Car
test_bike = FlyingBike() # Flying Bike

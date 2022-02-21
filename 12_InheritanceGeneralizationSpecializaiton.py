# inheritance generalization and specialization examples

# generalization case
# class Deposit adds currency assignment which is not supported by its parent class EuroDeposit
class EuroDeposit():
    def __init__(self):
        print("Currency is euro")

class Deposit(EuroDeposit):
    def __init__(self, currency):
        self.currency = currency
        print(f"Currency is {self.currency}")

euro_deposit = EuroDeposit() # Currency is euro
general_deposit_USD = Deposit("USD") # Currency is USD
general_deposit_RUB = Deposit("RUB") # Currency is RUB



# specialization case
# PrintMenu class narrows Menu class

class Menu():
    def __init__(self):
        print("General menu --> ")


class PrintMenu(Menu):
    def __init__(self):
        super().__init__()
        print("Print menu")

m1 = Menu() # General menu --> 
m2 = PrintMenu() # General menu --> Print menu


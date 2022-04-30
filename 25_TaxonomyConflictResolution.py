"""
Иерархия меню
Базовое меню BaseMenu принимает имя и выводит его.
Другие типы меню (таблица TableMenu и дерево TreeMenu) принимают имя и выводят свой тип.
"""

class BaseMenu():
    name = ""

    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        print(f"Menu name is: {self.name}")


class TableMenu(BaseMenu):
    type = "Table"

    def display_info(self):
         super().display_info()
         print(f"Menu type is: {self.type}")


class TreeMenu(BaseMenu):
    type = "Tree"

    def display_info(self):
         super().display_info()
         print(f"Menu type is: {self.type}")


test = BaseMenu("BaseMenu")
test.display_info() # Menu name is: BaseMenu

test2 = TableMenu("TableMenu")
test2.display_info() # Menu name is: TableMenu
                     # Menu type is: Table

test3 = TreeMenu("TreeMenu")
test3.display_info() # Menu name is: TreeMenu
                     # Menu type is: Tree

"""
В Python нет возможности запретитить переопределять методы.
На практике используют договоренность:
простой комментарий перед методм
делают метод защищенным (одно подчеркивание) или закрытым (два подчеркивания) 
"""

# примеры трех способов в коде

class Base():
    def method(self):
        """don't override this method"""
        print('Public method')

    def _method(self):
        print('Protected method')

    def __method(self):
        print('Private method')

class Derived(Base):
    def method(self):
        print('overriden public method')

    def _method(self):
        print('overriden protected method')
    
    def __method(self):
        print('overriden private method')

base_obj = Base()
base_obj.method() # Public method
base_obj._method() # Protected method
#base_obj.__method() # 'Base' object has no attribute '__method'

derived_obj = Derived()
derived_obj.method() # overriden public method
derived_obj._method() # overriden protected method
#derived_obj.__method() # 'Derived' object has no attribute '__method'
"""
Приведите пример иерархии, которая реализует наследование вида.

В качестве примера хорошо подойдет классификация видов тестирования.

Например, тесты могут быть:
1. по уровню тестирования - модульными, интеграционными, системными
2. по степени автоматизации - ручными, автоматическими
3. по работе с приложением - позитивными, негативными

Возможно множество других критериев классификации, причем единственный главный критерий выявить сложно.

В итоге конкретный тест может получиться:
1. системным автоматическим позитивным,
2. ручным интеграционным негативным,
3. системным ручными позитивным
4. и так далее.
"""


class TestingLevel:
    pass

class AutomationLevel:
    pass

class WorkLevel:
    pass


class ActualTest(TestingLevel, AutomationLevel, WorkLevel):
    pass

"""
1. Новый модуль может задавать некоторый базовый тип, который потенциально должен допускать параметризацию другими типами
В Python такое реализуется с помощью аннотации типов.

2. Новый модуль может объединять несколько функций, которые активно обращаются друг к другу
В Python такое возможно, создать общий модуль, а внутри него функции.

3. Новый модуль может входить в семейство модулей, ориентированных на решение некоторой общей задачи
Например, в Python есть встроенный модуль math. В нем собраны функции для решения математическиз задач.

4. Новый модуль может предлагать конкретную реализацию родительского модуля, которая должна выбираться динамически
В Python такое реализуется с помощью аннотации типов.

5. Новый модуль может интегрировать общее поведение нескольких модулей, которые различаются лишь деталями.
Не уверен, что такое есть в Python.

"""
"""
пример абстрагирования
(создан универсальный класс, далее обнаруживается, что это специфический случай,
лучше добавить этому классу предка и организовать наследование).

Для древовидного меню создан класс TreeMenu, далее возникает табличное меню TableMenu,
становится ясно, что лучше наиболее общие действия для меню (например, закрыть, свернуть)
вынести в класс-предок BaseMenu и уже от него наследовать TreeMenu и TableMenu/


пример факторизации
(несколько на первый взгляд несвязанных классов представляют собой лишь частные случаи одного понятия)

Например, классы ЖесткийДиск, ТвердотельныйНакопитель, Дискета, CDRW, DVDR реализуют понятие "носитель данных".
"""
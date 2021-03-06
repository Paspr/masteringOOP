"""
1. Существуют ли ситуации, когда связи между модулями должны делаться публичными?
В общем случае скорее всего нежелательно делать публичные связи.
При крайней необходимости можно сделать одни модули только читающими данные,другие - только записывающими данные. 

2.Какие метрики вы бы предложили для количественной оценки принципов организации модулей?
Наверное ограничение на количество элементов - классов, методов в них, количество самих модулей.

3. Если вы разрабатывали программы, в которых было хотя бы 3-5 классов, как бы вы оценили их модульность по этим метрикам?
В этом случае - количество классов (5) допустимое, в каждом классе желательно (например) не больше 20 методов,
сами методы желательно держать максимально короткими (например, 50 строк кода).

"""
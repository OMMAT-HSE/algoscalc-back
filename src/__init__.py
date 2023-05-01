"""Реализация API для онлайн-калькулятора.

API предоставляет доступ к алгоритмам. Получить список имеющихся алгоритмов
можно посредством выполнения GET запроса к конечной точке /api/algorithms.
Ответ содержит экземпляр класса Algorithms.

Доступ к конкретному алгоритму осуществляется по URI
/api/algorithms/{algorithm_name}, с указанием уникального имени алгоритма.
Получить описание выбранного алгоритма можно посредством выполнения GET
запроса к конечной точке /api/algorithms/{algorithm_name}. Ответ содержит
экземпляр класса AnswerAlgorithmDefinition.

Получить результат выполнения алгоритма можно посредством выполнения POST
запроса к конечной точке /api/algorithms/{algorithm_name}, с передачей
фактических значений для набора входных параметров - с помощью объекта
класса Parameters. Ответ содержит экземпляр класса AnswerOutputs.

+--------+---------------------------+---------------------------------------+
| Запрос | Конечная точка            | Действие                              |
+========+===========================+=======================================+
| GET    | /api/algorithms           | Получить список имеющихся алгоритмов  |
+--------+---------------------------+---------------------------------------+
| GET    | /api/algorithms/fibonacci | Получить описание алгоритма fibonacci |
+--------+---------------------------+---------------------------------------+
| POST   | /api/algorithms/fibonacci | Выполнить алгоритм fibonacci          |
+--------+---------------------------+---------------------------------------+

"""
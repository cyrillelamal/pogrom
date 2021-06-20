> > Создание пользовательского пакета с организованным в нем механизмом «фасад» для импорта модулей. Публикация собственного пакета в общем репозитории пакетов pypi.

# varseries

[varseries](https://pypi.org/project/varseries/)

Этот модуль был разработан, чтобы комфортно выполнить лабораторные работы по дисциплине
"Анализ данных" на втором курсе.

[`__init__.py`](https://github.com/cyrillelamal/varseries/blob/master/src/varseries/__init__.py) выступает в качестве "
фасада", хотя и не является реализацией паттерна проектирования "фасад".

Без `__init__.py` импорт происходит следующим образом:

```python
from varseries.varseries import DiscreteVS
```

А с фасадом `__init__.py`:

```python
from varseries import DiscreteVS
```

Это ожидаемое поведение для всех сторонних библиотек.

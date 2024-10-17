# Домашнее задание по уроку "Пространство имен"


def test_function():
    def inner_function():
        print( "Я в области видимости функции test_function")
    inner_function()
# Вызов функции inner_function() за локальной областью функции test_function() не возможен.
test_function()

import math
import random


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = (a + b) * 2
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b
    assert area == 200

    print(f"Периметр прямоугольника с длиной {a} и шириной {b} = {perimeter},а площадь = {area}")

def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = r**2 * math.pi
    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = r*2 * math.pi
    assert length == 144.51326206513048

    print(f" Площадь окружности с радиусом {r} = {area},а длина = {length}")


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # TODO создайте список
    l = []
    for x in range(10):
        m = random.randint(0, 101)
        x = x + 1
        l.insert(x, m)
        l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    # TODO удалите повторяющиеся элементы

    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    ziped = zip(first, second)
    d = dict(ziped)
    print(d)

    assert isinstance(d, dict)
    assert len(d) == 5
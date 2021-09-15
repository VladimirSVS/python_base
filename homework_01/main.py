"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    squares_nums = []
    for num in nums:
        if isinstance(num, int) and num >= 0:
            squares_nums.append(num ** 2)
    return squares_nums


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    """
    Функция, на вход принимает число,
    проверяет простое число или нет, и 
    возвращает True - простое,
    False - составное.

    >>> is_prime(5)
    <<< True
    >>> is_prime(4)
    <<< False
    """
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    if d * d > num and num != 1:
        return True
    else:
        return False


def filter_numbers(nums, num_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    filters = { ODD:{ 'func': lambda num: (num % 2) == 1 },
                EVEN: { 'func': lambda num: (num % 2) == 0 },
                PRIME: { 'func': is_prime }
                }
    if isinstance(nums,(tuple, list)) and num_type in filters.keys():
        return list(filter(filters[num_type]['func'], nums))

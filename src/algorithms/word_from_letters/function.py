import time

import pymorphy3


LENGTH_LIMIT = 7
"""Предельная длина строки"""
WORDS = 'words'
"""Ключ для словаря с результатом работы функции main"""


def generate_permutations(letters_str: str) -> list[str]:
    """Генерирует все варианты перестановок символов указанной строки
    :param letters_str: входящая строка
    :return: список перестановок символов входящей строки, где каждая
    перестановка строка, содержащая указанные символы
    """
    pass


def main(letters: str):
    """Генерирует слова, составленные из символов входящей строки. Из символов
    генерируются все возможные перестановки, которые проверяются через словарь
    с помощью библиотеки pymorphy3
    :param letters: входящая строка
    :raise TypeError: если параметр не является строкой
    :raise ValueError: если входящая строка содержит пробел или ее длина
    превышает максимально возможное значение
    :return: список слов
    """
    pass


if __name__ == '__main__':
    letters = 'abc'
    print(generate_permutations(letters))

    start_time = time.time()
    letters = 'Поледар'
    print(main(letters))
    print(f'duration: {time.time() - start_time} seconds')

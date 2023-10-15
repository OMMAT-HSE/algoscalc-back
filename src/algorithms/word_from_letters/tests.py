import unittest


from src.algorithms.word_from_letters.function import (generate_permutations,
                                                       main, LENGTH_LIMIT,
                                                       WORDS)


class TestCase(unittest.TestCase):
    def test_incorrect_inputs(self):
        """Проверка выброса TypeError исключения при передаче
        в параметр некорректного значения"""
        err_msg = 'Переданный параметр не является строкой'
        incorrect_inputs = (None, 1, 1.1, True, [1, 2, 3], {1, 2, 3},
                            (1, 2, 3))
        for val in incorrect_inputs:
            self.assertRaisesRegex(TypeError, err_msg,
                                   main, val)

    def test_over_length(self):
        """Проверка выброса ValueError исключения при передаче
        в параметр излишне длинной строки"""
        err_msg = f'Длина введенной строки превышает {LENGTH_LIMIT} символов'
        for i in range(1, 3):
            self.assertRaisesRegex(ValueError, err_msg, main,
                                   'a'*(LENGTH_LIMIT + i))

    def test_space(self):
        """Проверка выброса ValueError исключения при передаче
        в параметр строки с пробелом"""
        err_msg = 'Введенная строка содержит пробел'
        strings = [' ', '  ', ' str', 'str ', 'st r', 's t r']
        for string in strings:
            self.assertRaisesRegex(ValueError, err_msg, main, string)

    def test_empty(self):
        """Проверка генерации перестановок для пустой сроки"""
        self.assertCountEqual([''], generate_permutations(''))

    def test_single_num(self):
        """Проверка генерации перестановок для строки из одного символа"""
        self.assertCountEqual(['1'], generate_permutations('1'))

    def test_double_num(self):
        """Проверка генерации перестановок для множества из двух чисел"""
        self.assertCountEqual(['12', '21'], generate_permutations('12'))

    def test_triple_char(self):
        """Проверка генерации перестановок для строки из трех символов"""
        self.assertCountEqual(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],
                              generate_permutations('abc'))

    def test_quadruple_num(self):
        """Проверка генерации перестановок для строки из четырех символов"""
        self.assertCountEqual(['1234', '1243', '1324', '1342', '1423',
                               '1432', '2134', '2143', '2314', '2341', '2413',
                               '2431', '3124', '3142', '3214', '3241', '3412',
                               '3421', '4123', '4132', '4213', '4231', '4312',
                               '4321'],
                              generate_permutations('1234'))

    def test_no_words(self):
        """Проверка строки, для которой нет слов"""
        self.assertCountEqual([], main('ыыы')[WORDS])

    def test_word(self):
        """Проверка строки, для которой есть одно слово"""
        self.assertCountEqual(['буйвол'], main('ловбуй')[WORDS])

    def test_upper_word(self):
        """Проверка строки с заглавными буквами, для которой есть одно слово"""
        self.assertCountEqual(['кролик'], main('ЛИКРОК')[WORDS])

    def test_few_words(self):
        """Проверка строки, для которой есть несколько слов"""
        result = main('поледар')[WORDS]
        self.assertIn('леопард', result)
        self.assertIn('порадел', result)


if __name__ == '__main__':
    unittest.main()

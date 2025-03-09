import unittest
import bubblesort
from unittest.mock import patch
import random

class TestBubbleSort(unittest.TestCase):

    # тест на пустой список
    def test_empty_list(self):
        self.assertEqual(bubblesort.bubble_sort([]), [])

    # тест на отсортированный массив
    def test_sorted_list(self):
        self.assertEqual(bubblesort.bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    # тест на обратноотсортированный массив
    def test_reverse_sorted_list(self):
        self.assertEqual(bubblesort.bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        
    # тест на частично упорядоченный массив
    def test_partially_ordered(self):
        self.assertEqual(bubblesort.bubble_sort([6, 8, 1, 2, 9, 10, 11, 12]), [1, 2, 6, 8, 9, 10, 11, 12])

    # тест на массив с повторяющимися элементами
    def test_repeated_elements(self):
        self.assertEqual(bubblesort.bubble_sort([3, 3, 4, 2, 5, 5, 2]), [2, 2, 3, 3, 4, 5, 5])

    # тест на массив, все значения которого одинаковы
    def test_same_value(self):
        self.assertEqual(bubblesort.bubble_sort([5, 5, 5, 5, 5, 5, 5, 5]), [5, 5, 5, 5, 5, 5, 5, 5])

    # тест на массив с отрицательными числами
    def test_negative_value(self):
        self.assertEqual(bubblesort.bubble_sort([5, -1, 9, 0, -6]), [-6, -1, 0, 5, 9])

    # тест на массив большого размера
    def test_big_size(self):
        self.assertEqual(bubblesort.bubble_sort([5, 1, 7, 98, 65, 75, 21, 97, 34, 96, 82, 74, 25, 16, 99, 12, 0, 3]), [0, 1, 3, 5, 7, 12, 16, 21, 25, 34, 65, 74, 75, 82, 96, 97, 98, 99])

    # тест на обработку случайных значений
    @patch('random.randint')
    @patch('bubblesort.generate_random_list')
    def test_random_list(self, mock_generate_random_list, mock_random):
        mock_generate_random_list.return_value = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(bubblesort.bubble_sort(bubblesort.generate_random_list(11)), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    # тест на то, что функция генерирует один список
    @patch('bubblesort.generate_random_list')
    def test_generate_random_list_called_once(self, mock_generate_random_list):
        bubblesort.bubble_sort(bubblesort.generate_random_list(5))  
        mock_generate_random_list.assert_called_once()

if __name__ == '__main__':
    unittest.main()
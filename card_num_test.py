import unittest
from BankCard import CardNum


class TestCardNum(unittest.TestCase):  # test class
    def setUp(self):
        self.card_number = CardNum()

    def test_valid_num(self):
        result = str(self.card_number.data_from_file('test_data/test_input.txt')).strip()
        self.assertIn('2200 1234 1234 1234', result)

    def test_invalid_num(self):
        result = self.card_number.data_from_file('test_data/test_input.txt')
        self.assertNotIn('invalid_number', result)

    def test_empty_file(self):
        result = self.card_number.data_from_file('test_data/empty_file.txt')
        self.assertEqual(result, [])

    def test_non_num_input(self):
        result = self.card_number.data_from_file('test_data/non_num_input.txt')
        self.assertEqual(result, [])

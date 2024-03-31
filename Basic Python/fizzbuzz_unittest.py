import unittest
from FizzBuzz import fizzbuzz
import pytest


class MyTestCase(unittest.TestCase):
    def test_fizzbuzz(self):
        assert fizzbuzz(6) == [1, 2, 'Fizz', 4, 'Buzz']
        assert fizzbuzz(0) == []
        assert fizzbuzz(1) == []
        assert fizzbuzz(2) == [1]
        assert fizzbuzz(22) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz']
        assert fizzbuzz(-2) == []

    def test_str(self):
        with pytest.raises(TypeError):
            fizzbuzz("cat")

if __name__ == '__main__':
    unittest.main()

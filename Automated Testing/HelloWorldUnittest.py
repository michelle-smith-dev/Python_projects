import unittest
from HelloWorld import hello


class MyTestCase(unittest.TestCase):
    def test_hello(self):
        assert hello() == "hello, world"
        assert hello("Michelle") == "hello, Michelle"

    def test_argument(self):
        for name in ["Hermoine", "Harry", "Ron"]:
            assert hello(name) == f"hello, {name}"


if __name__ == '__main__':
    unittest.main()

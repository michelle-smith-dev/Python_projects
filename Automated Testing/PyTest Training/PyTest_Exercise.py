import os
import sys
import pytest
import unittest
import itertools
from ddt import ddt, data, file_data, idata, unpack
# Need to search 'ddt' in Python Packages in bottom left, to install module

# # basic tests
# def divide(x, y):
#     return x/y
#
#
# def test_raises():
#     with pytest.raises(ZeroDivisionError):
#         divide(3, 0)
#
#
# # Can use match to assert the error matches with the string we provide
# def divide1(x: str, y: str):
#     int(x) / int(y)
#     return x, y
#
#
# def test_divide():
#     with pytest.raises(ValueError, match="invalid literal for int"):
#         divide1("a", "2")
#
#
# # Use built in marks to decorate a test. The parametrize allows us to pass in data to a test function without hard
# # coding that data inside the function
# @pytest.mark.parametrize("num", [2, 4, 6])
# def test_is_even(num):
#     assert num % 2 == 0
#
#
# @pytest.mark.parametrize("first, second", [
#     (1, 2),
#     (2, 3),
#     (3, 4),
# ])
# def test_successor(first, second):
#     assert first + 1 == second
#
#
# # Use marker to skip a test
# @pytest.mark.skip()
# def test_skip_me():
#     assert 2 + 2 == 4
#
#
# # Use marker to xpass a test, knowing it will fail
# @pytest.mark.xfail()
# def test_failure():
#     assert 4/2 == 3
#
#
# @pytest.mark.parametrize("first, second", [
#     (2, 2),
#     (3, 3),
#     (4, 4)
# ])
# def test_divide_param(first, second):
#     assert first / second == 1
#
#
# # Fixtures
# @pytest.fixture
# def answer():
#     # pytest.skip("Server is not available.")
#     return 42
#
#
# @pytest.fixture
# def answer2():
#     return 23
#
#
# def test_universe(answer, answer2):
#     assert answer == 42
#     assert answer2 == 23


# # Builtin fixtures/tmp_path
# @pytest.fixture
# def input_file(tmp_path):  # The tmp_path is builtin, and this is the path it created:
#     #  C:\Users\msmith\AppData\Local\Temp\pytest-of-MSmith\pytest-4\test_things0\input.txt
#     path = tmp_path / "input.txt"
#     path.write_text("Hello, World")
#     return path
#
#
# def test_things(input_file):
#     assert True, str(input_file)
#     # Asserting this as True means the path returned from the input_file function is a string. Which when I run it to
#     # assert as False, I can see that it does, in fact, return as a string value:
#     # input_file = WindowsPath('C:/Users/msmith/AppData/Local/Temp/pytest-of-MSmith/pytest-4/test_things0/input.txt')


# Builtin fixtures/monkeypatch
def func():
    path = os.environ.get("PATH", "")
    print(f"platform: {sys.platform}")
    print(f"PATH: {path}")

# Test monkeypatching the func function: platform: MonkeyOS
# PATH: /zoo
def test_one(monkeypatch):
    monkeypatch.setattr(sys, "platform", "MonkeyOS")
    monkeypatch.setenv("PATH", "/zoo")
    func()
    assert True


# Test the second test is starting as a fresh instance because monkeypatch tearsdown the setup
# platform: win32
# PATH: C:\Users\msmith\github\temp_project\venv\Scripts
def test_two():
    func()
    assert True


@ddt
class DataDrivenTests:

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @data(["Anna", "Bayer"], ["Mark", "Darcy"], [None, "Jones"])
    def test_should_validate_names_and_surnames(self, name, surname):
        assert name is not None
        assert surname is not None

import pytest
import add_scratch


def test_add():
    assert add_scratch.add(5, 5) == 10
    assert add_scratch.add(5) == 7


def test_multiply():
    assert add_scratch.multiply(5, 5) == 25
    assert add_scratch.multiply(2) == 4


def test_add_string():
    result = add_scratch.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'sds' not in result
    assert 'ell' in result
    assert 'llrld' not in result


def test_multiply_string():
    assert add_scratch.multiply('Hello ', 3) == 'Hello Hello Hello '
    result = add_scratch.multiply('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result


# Test with parametrize
''' Instead of the following code:
def test_add():
    assert add_scratch.add(7, 3) == 10
    
def test_add_strings():
    result = add_scratch.add('Hello', ' World')
    assert result == 'Hello World'
    
def test_add_float():
    result = add_scratch.add(10.5, 25.5)
    assert result == 36

We can write the above using parametrize
'''


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 10),
                             ('Hello', ' World', 'Hello World'),
                             (10.5, 25.5, 36)
                         ]
                         )
def test_add_numbers(num1, num2, result):
    assert add_scratch.add(num1, num2) == result

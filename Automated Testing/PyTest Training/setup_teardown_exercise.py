import pytest


def multiply(x, y):
    return x * y


@pytest.fixture
def setup():
    print("--------Setup--------")
    lst = []
    for i in range(5):  # [(0, 0, 0), (1, 2, 2), (2, 4, 8), (3, 6, 18), (4, 8, 32)]
        lst.append((i, i*2, i*i*2))

    yield lst
    print("--------Teardown--------")
    lst = []


def test_multiply(setup):  # setup = lst
    for i in setup:
        assert multiply(i[0], i[1]) == i[2]

# lst = []
# for i in range(10):
#     lst.append((i, i*2, i*i*2))
# print(lst)
from shopping_cart import ShoppingCart
from shopping_cart_database import ItemDatabase
import pytest
from unittest.mock import patch, MagicMock, Mock


# def test_can_add_item_to_cart():
#     cart = ShoppingCart(5)
#     cart.add("apple")
#     assert cart.size() == 1
#
#
# def test_when_item_added_then_cart_contains_item():
#     cart = ShoppingCart(5)
#     cart.add("apple")
#     assert "apple" in cart.get_items()
#
#
# def test_max_items_fail():
#     cart = ShoppingCart(5)
#     for i in range(5):
#         cart.add("apple")
#     with pytest.raises(OverflowError):
#         cart.add("apple")
#
#
# def test_can_get_total_price():
#     cart = ShoppingCart(5)
#     cart.add("apple")
#     cart.add("orange")
#
#     price_map = {"apple": 1.0, "orange": 2.0}
#
#     assert cart.get_total_price(price_map)


 # Now let's rewrite the above to show how fixtures can be very useful
@pytest.fixture
def cart():
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_max_items_fail(cart):
    for i in range(5):
        cart.add("apple")
    with pytest.raises(OverflowError):
        cart.add("apple")

# This is the original function where we are creating our own price_map
# def test_can_get_total_price(cart):
#     cart.add("apple")
#     cart.add("orange")
#     price_map = {"apple": 1.0, "orange": 2.0}
#     assert cart.get_total_price(price_map)


# This function is created to show mocking a database that isn't quite finish but is created
def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    # Create a mock function within the scope to call using side_effect
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0

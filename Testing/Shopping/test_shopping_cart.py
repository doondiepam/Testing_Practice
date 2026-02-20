
from Testing_Practice.Testing.Shopping.shopping_cart import ShoppingCart
import pytest

def test_cart_creation():
    cart = ShoppingCart()
    assert cart.items == {}

def test_add_item_success():
    cart = ShoppingCart()
    cart.add_item("Book", 100, 2)

    assert "Book" in cart.items
    assert cart.items["Book"]["price"] == 100
    assert cart.items["Book"]["quantity"] == 2

def test_invalid_price():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("pen",0,1)

def test_invalid_Quantity():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("pen",1,0)

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("book",100,1)
    cart.remove_item("book")

    assert "Book" not in cart.items
    

def test_item_notfound_for_removing():
    cart = ShoppingCart()
    with pytest.raises(KeyError):
        cart.remove_item("phone")

def test_get_total():
    cart = ShoppingCart()
    cart.add_item("Book", 100, 2)   
    cart.add_item("Pen", 10, 3)     

    assert cart.get_total() == 230

def test_clear_cart():
    cart = ShoppingCart()
    cart.add_item("Book", 100, 1)
    cart.clear_cart()

    assert cart.items == {}


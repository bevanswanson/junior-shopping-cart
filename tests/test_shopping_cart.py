import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shopping_cart import greet, add_to_cart


# Greet
def test_greet():
    # act
    result = greet('Alice')

    # assert
    assert result == 'Hello, Alice!'


# Add to cart
def test_add_to_cart():
    # arrange
    cart = []

    # act
    result = add_to_cart('Apple', cart)

    # assert
    assert result == 'Adding Apple to cart.'
    assert 'Apple' in cart
    assert len(cart) == 1

def test_add_to_cart_multiple_items():
    # arrange
    cart = []

    # act
    result1 = add_to_cart('Banana', cart)
    result2 = add_to_cart('Orange', cart)

    # assert
    assert result1 == 'Adding Banana to cart.'
    assert result2 == 'Adding Orange to cart.'
    assert 'Banana' in cart
    assert 'Orange' in cart
    assert len(cart) == 2

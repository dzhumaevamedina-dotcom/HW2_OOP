import pytest
from recipe import Ingredient

def test_ingredient_creation():
    item = Ingredient("Myka", 500, "r")
    assert item.quantity == 500.0

def test_ingredient_quantity_validation():
    prod = Ingredient("Myka", 500, "r")
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        prod.quantity = -10

def test_ingredient_str():
    item = Ingredient("Myka", 500, "r")
    assert str(item) == "Myka: 500.0 r"

def test_ingredient_repr():
    item = Ingredient("Myka", 500, "r")
    assert repr(item) == "Ingredient('Myka', 500.0, 'r')"

def test_ingredient_eq():
    i1 = Ingredient("Myka", 500, "r")
    i2 = Ingredient("Myka", 1000, "r")
    i3 = Ingredient("Caxap", 500, "r")
    i4 = Ingredient("Myka", 500, "kr")
    
    assert i1 == i2
    assert i1 != i3
    assert i1 != i4
import pytest

import source.my_functions as my_functions


def test_add():
    result = my_functions.add(x=1,y=4)

    assert result == 5

def test_add_strings():
    result = my_functions.add(x="I like ", y="burgers")
    assert result == "I like burgers"


def test_divide():
    result = my_functions.divide(x=10,y=2)
    assert result == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(x=10,y=0)
    

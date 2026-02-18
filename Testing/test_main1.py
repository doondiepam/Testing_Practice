
from Main1 import add 
from Main1 import divide
import pytest

def test_add():
    assert add(2,3) == 5
    assert add(3,4) == 7
    assert add(1,2) == 3

def test_divid():
    assert divide(2,2) == 1
    assert divide(20,10) == 2

def test_divid_zero():
    with pytest.raises(ValueError):
        divide(20,0)

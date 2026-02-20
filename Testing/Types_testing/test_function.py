
from Testing_Practice.Testing.Types_testing.Main1 import add, sub, multiply, divide

def test_all_functions():
    assert add(2,3) == 5
    assert sub(4,4) == 0
    assert multiply(3,3) == 9
    assert divide(4,2) == 2


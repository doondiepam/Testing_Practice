from Testing_Practice.Testing.Types_testing.intergration_testexample import add, multiply

def test_add_multi():
    res = multiply(add(2,3), 5)
    assert res == 25
    
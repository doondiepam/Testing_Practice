"""
Create a fixture account
Write tests for:
deposit success
deposit negative
withdraw success
withdraw insufficient
withdraw zero
Goal: 👉 Each test must start with fresh balance 1000.
"""
from acc import Account
import pytest

@pytest.fixture
def acc():
    return Account()

def test_doposite_success(acc):
    assert acc.deposit(200) == 1200
    pass

def test_negitive_deposite(acc):
    with pytest.raises(ValueError):
        assert acc.deposit(-1)

def test_withdrw_success(acc):
    assert acc.withdraw(200) == 800

def test_insuffiesent_funds(acc):
    with pytest.raises(ValueError):
        assert acc.withdraw(2000)

def test_withdrew_zero(acc):
    with pytest.raises(ValueError):
        assert acc.withdraw(0)








# from bank import BankAccount
from bank import BankAccount
import pytest 


@pytest.fixture
def account():
    return BankAccount("vivek",1000)
@pytest.fixture
def two_acc():
    acc1 = BankAccount("vivek", 1000)
    acc2 = BankAccount("ram", 500)
    return acc1,acc2
def test_account_creation(account):
    assert account.owner == "vivek"
    assert account.balance == 1000
def test_deposite_scesses(account):
    assert account.deposit(200) == 1200
    assert account.balance == 1200
def test_invalid_ammount(account):
    with pytest.raises(ValueError):
        account.deposit(0)
def test_withdraw_scusses(account):
    assert account.withdraw(200) == 800
    assert account.balance == 800
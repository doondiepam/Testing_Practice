
from bank import BankAccount
import pytest

def test_check_accountcreation_success():
    acc = BankAccount("vivek", 1000)
    assert acc.owner == "vivek"
    assert acc.balance == 1000

def test_check_deposite_sucesses():
    acc = BankAccount("Vivek", 100)
    assert acc.deposit(50) == 150
    assert acc.balance == 150

def test_deposite_invalid_ammount():
    acc = BankAccount("Vivek", 100)
    with pytest.raises(ValueError):
        acc.deposit(0)

def test_withdraw_sucesses():
    acc = BankAccount("Vivek", 100)
    assert acc.withdraw(50) == 50
    assert acc.balance == 50

def test_withdraw_ammount_notsufficent():
    acc = BankAccount("Vivek", 100)
    with pytest.raises(ValueError):
        acc.withdraw(200)

def test_tansfer_sucess():
    acc1 = BankAccount("Vivek", 100)
    acc2 = BankAccount("Mohitha", 100)

    acc1.transfer(acc2,50)

    assert acc1.balance == 50
    assert acc2.balance == 150

def test_invalid_transfer():
    acc1 = BankAccount("Vivek", 100)
    with pytest.raises(TypeError):
        acc1.transfer("Invalid account", 50)


# def test_all_func():
    
#     acc1 = BankAccount("vivek", 1000)
#     acc2 = BankAccount("Ram",600)

#     acc1.deposit(500)
    
#     acc1.transfer(acc2,100)

#     acc2.withdraw(400)

#     assert acc1.balance == 1400
#     assert acc2.balance == 300


def test_balance(account):
    assert account["balance"] == 1000


def test_transaction(transaction):
    assert transaction == 800


import pytest

@pytest.fixture(scope="session")
def account():
    print("Create account")
    yield {"balance": 1000}
    print("Destroy account")


@pytest.fixture
def username():
    return "vivek"

@pytest.fixture
def user(username):
    return {"name": username,"balance":1000}

@pytest.fixture
def transaction(user):
    print("before balance",user)
    user["balance"] -= 200
    yield user["balance"]
    print("after update",user)




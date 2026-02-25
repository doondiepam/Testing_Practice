from typing import Optional

users = {}

def add_user(username: str, password: str):
    users[username] == password

def get_user(username: str) -> Optional[str]:
    return users.get(username)
    pass

def remove_user(username: str) -> None:
    users.pop(username, None)

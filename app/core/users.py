from app.core.auth import hash_password, verify_password

USERS = {
    "admin": {
        "id": "user-1",
        "username": "admin",
        "password": hash_password("admin123")
    }
}

def authenticate(username: str, password: str):
    user = USERS.get(username)
    if not user:
        return None
    if not verify_password(password, user["password"]):
        return None
    return user

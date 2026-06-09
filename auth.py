from jose import jwt

SECRET_KEY = "SUPER_SECRET_KEY"

def create_access_token(email):

    token = jwt.encode(
        {"sub": email},
        SECRET_KEY,
        algorithm="HS256"
    )

    return token

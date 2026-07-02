from passlib.context import CryptContext

from jose import jwt
from datetime import datetime, timedelta

from jose import JWTError
from fastapi import HTTPException, status

SECRET_KEY = "mysecretkey123"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_password_hash(password: str):

    return pwd_context.hash(password)


def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def verify_access_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

# bcrypt is preferred because it is intentionally slow,
# making brute-force attacks difficult.
# MD5 and SHA-256 are fast hashing algorithms and are not
# suitable for password storage.
# Never store plain-text passwords.

# OAuth2 Authorization Code Flow:
# Used by applications that authenticate users through an external
# Identity Provider (Google, Microsoft, GitHub, etc.).
# The user logs in with the provider, which returns an authorization code.
# The application exchanges the code for an access token.

# JWT Login (implemented here):
# The application verifies the user's email and password directly.
# After successful authentication, it creates and returns a JWT token.
# The client sends this token in the Authorization header
# for all protected requests.
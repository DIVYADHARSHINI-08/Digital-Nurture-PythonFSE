from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from schemas import (
    UserRegister,
    UserLogin,
    UserResponse
)
from security import (
    get_password_hash,
    verify_password,
    create_access_token,
    verify_access_token
)

from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = []


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login/"
)


@app.get("/")
async def root():
    return {"message": "Authentication API Running"}

@app.post(
    "/api/v1/auth/register/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def register(user: UserRegister):

    # Check if email already exists
    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=409,
                detail="Email already registered"
            )

    # Hash the password
    hashed_password = get_password_hash(user.password)

    # Create user
    new_user = {
        "id": len(users) + 1,
        "email": user.email,
        "hashed_password": hashed_password,
        "is_active": True
    }

    users.append(new_user)

    return {
        "id": new_user["id"],
        "email": new_user["email"],
        "is_active": new_user["is_active"]
    }

@app.post("/api/v1/auth/login/")
async def login(user: UserLogin):

    for existing_user in users:

        if existing_user["email"] == user.email:

            if verify_password(
                user.password,
                existing_user["hashed_password"]
            ):

                token = create_access_token(
                    {
                        "sub": existing_user["email"]
                    }
                )

                return {
                    "access_token": token,
                    "token_type": "bearer"
                }

            break

    raise HTTPException(
        status_code=401,
        detail="Invalid email or password"
    )
async def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    payload = verify_access_token(token)

    email = payload.get("sub")

    for user in users:

        if user["email"] == email:
            return user

    raise HTTPException(
        status_code=401,
        detail="User not found"
    )
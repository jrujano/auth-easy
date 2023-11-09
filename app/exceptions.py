from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED


class HandlerExceptions:
    def __init__(self):
        pass

    @staticmethod
    def InvalidCredentialsException():
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    @staticmethod
    def DuplicateEmailException():
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Email not valid",
            headers={"WWW-Authenticate": "Bearer"},
        )


# InvalidCredentialsException =

from fastapi import Header, HTTPException
from http import HTTPStatus
import pyjwt

async def get_token_header(token: str = Header(...)):
    try:

        return True
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Unauthorized")

    # if bearer != "token":
    #     raise HTTPException(status_code=400, detail="Unauthorized")



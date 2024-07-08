import json
# import pytest
from app.common.authentication import get_token_header
import pytest
import pyjwt


@pytest.mark.asyncio
async def test_authentication():

    available_token = 'Bearer a1b2c3d4e5f6g7'
    improper_token = 'baba a1b2c3d4e5f6g7'
    not_bearer_token = 'a1b2c3d4e5f6g7'

    available_result = await get_token_header(available_token)
    improper_result = await get_token_header(improper_token)
    not_bearer_result = await get_token_header(not_bearer_token)

    assert result == True
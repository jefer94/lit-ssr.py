

from typing import Any
import aiofiles
import httpx

from .defaults import TIMEOUT
from .exceptions import Timeout, UnexpectedException
from ..settings import host


async def arender() -> Any:
    async with aiofiles.open('filename', mode='r') as f:
        contents = await f.read()

    async with httpx.AsyncClient(http2=True) as client:
        try:
            response = await client.post(host, timeout=TIMEOUT)
            json = response.json()

        except httpx.TimeoutException:
            return Timeout('timeout')

        except Exception as e:
            return UnexpectedException(str(e))

        return json


def render() -> Any:
    with open('filename', mode='r') as f:
        contents = f.read()

    try:
        response = httpx.post(host, timeout=TIMEOUT)
        json = response.json()

    except httpx.TimeoutException:
        return Timeout('timeout')

    except Exception:
        return UnexpectedException('timeout', status=408)

    return json

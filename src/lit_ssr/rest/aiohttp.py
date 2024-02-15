

from typing import Any
import aiofiles
import aiohttp

from .defaults import TIMEOUT
from .exceptions import Timeout, UnexpectedException
from ..settings import host


async def arender() -> Any:
    async with aiofiles.open('filename', mode='r') as f:
        contents = await f.read()

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(host, timeout=TIMEOUT) as response:
                json = await response.json()

    except aiohttp.ClientTimeoutError:
        return Timeout('timeout')

    except Exception as e:
        return UnexpectedException(str(e))

    return json

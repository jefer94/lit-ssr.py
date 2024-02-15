
from typing import Any
import aiofiles
import requests

from .defaults import TIMEOUT
from .exceptions import Timeout, UnexpectedException
from ..settings import host


async def arender() -> Any:
    async with aiofiles.open('filename', mode='r') as f:
        contents = await f.read()

    try:
        response = requests.get(host, timeout=TIMEOUT)
        json = response.json()

    except requests.Timeout:
        return Timeout('timeout')

    except Exception as e:
        return UnexpectedException(str(e))

    return json


def render() -> Any:
    with open('filename', mode='r') as f:
        contents = f.read()

    try:
        response = requests.get(host, timeout=TIMEOUT)
        json = response.json()

    except requests.Timeout:
        return Timeout('timeout')

    except Exception as e:
        return UnexpectedException(str(e))

    return json

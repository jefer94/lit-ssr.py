import re
import aiofiles

from typing import Optional, TypedDict

DEPENDENCY_PATTERN = re.compile(r'<!--\s?lit-ssr\sload\s([^\s]+)\s*?-->')

__all__ = ['render', 'arender']


class Dependency(TypedDict):
    code: str
    ext: int


def _validator(dependencies: Optional[list[Dependency]] = None, auto=False):
    if auto and dependencies is not None:
        raise ValueError("Cannot use auto=True and specify dependencies")


async def _aiterator(list: list):
    for item in list:
        yield item


def _discover_dependencies(html: str) -> list[Dependency]:
    dependencies = []
    matches = DEPENDENCY_PATTERN.findall(html)

    for match in matches:
        with open(match, mode='r') as file:
            ext = match[-2:]
            code = file.read()

            dependencies.append({'code': code, 'ext': ext})

    return dependencies


async def _adiscover_dependencies(html: str) -> list[Dependency]:
    dependencies = []
    matches = DEPENDENCY_PATTERN.findall(html)

    async for match in _aiterator(matches):
        async with aiofiles.open(match, mode='r') as file:
            ext = match[-2:]
            code = await file.read()

            dependencies.append({'code': code, 'ext': ext})

    return dependencies


# class SSR(object):
def render(html: str, dependencies: Optional[list[Dependency]] = None, auto: bool = False):
    from . import rest

    _validator(dependencies, auto)

    if auto:
        dependencies = _discover_dependencies()

    elif dependencies is None:
        dependencies = []

    return rest.render()


async def arender(html: str, dependencies: Optional[list[Dependency]] = None, auto = False):
    from . import rest

    _validator(dependencies, auto)

    if auto:
        dependencies = await _adiscover_dependencies()

    elif dependencies is None:
        dependencies = []

    return rest.arender()

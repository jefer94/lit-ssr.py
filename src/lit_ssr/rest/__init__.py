from .exceptions import NoClientInstalled

__all__ = ['arender', 'render']

try:
    import aiohttp  # noqa: F401
    from .aiohttp import arender

except ImportError:
    ...

try:
    import httpx  # noqa: F401

    if 'arender' not in globals():
        from .httpx import arender, render  # noqa: F811

    else:
        from .httpx import render  # noqa: F811


except ImportError:
    import requests  # noqa: F401

    if 'arender' not in globals():
        from .requests import arender, render  # noqa: F811

    else:
        from .requests import render

except ImportError:
    raise NoClientInstalled('No client installed')

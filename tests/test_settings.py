import pytest

# @pytest.fixture(autouse=True)
# async def server(anyio_backend):
#     yield

HOST = "http://localhost:3000"


def test_host():
    import src.lit_ssr.settings as settings
    assert settings.host == HOST


@pytest.mark.parametrize("new_host,result", [
    ("https://hatch.pypa.io/", "https://hatch.pypa.io"),
    ("https://www.google.com", "https://www.google.com"),
])
def test_set_host(new_host, result):
    import src.lit_ssr.settings as settings
    assert settings.set_host(new_host) is None
    assert settings.host == result

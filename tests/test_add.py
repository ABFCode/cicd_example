import pytest

from src.add import Add


@pytest.fixture
def add_fixture():
    return Add()


def test_add(add_fixture: Add):
    assert add_fixture.add(5, 8) == 13
    assert add_fixture.add(0, 0) == 0

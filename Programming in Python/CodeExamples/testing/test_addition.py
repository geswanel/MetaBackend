import pytest
import addition

@pytest.fixture
def numbers():
    return [(1, 2), (4, 5), (9, 10)]

def test_add(numbers):
    for a, b in numbers:
        assert addition.add(a, b) == a + b


@pytest.mark.xpass
def test_sub():
    assert addition.sub(4, 5) == -1

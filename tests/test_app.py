from app import add

def test_add():
    assert add(1, 3) == 4
    assert add(-1, 1) == 0
def test_zero_addition():
    assert add(0,7) == 7
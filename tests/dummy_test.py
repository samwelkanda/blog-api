def test_always_passes():
    assert True


def test_string():
    assert isinstance("2", str)


def test_sum():
    assert sum((1, 2, 3, 4, 5, 6, 7, 8, 9)) == 45

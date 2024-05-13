import to_test


def test_not_prime():
    assert to_test.simple_checking(10) is False


def test_prime():
    assert to_test.simple_checking(11) is True

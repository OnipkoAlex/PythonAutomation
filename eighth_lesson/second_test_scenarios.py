from eighth_lesson import to_test


def test_not_prime():
    """Scenario with not prime number"""
    assert to_test.simple_checking(10) is False


def test_prime():
    """Scenario with a prime number"""
    assert to_test.simple_checking(11) is True

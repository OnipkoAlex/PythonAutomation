from to_test import simple_checking


def test_not_prime():
    """Scenario with not prime number"""
    assert simple_checking(10) is False


def test_prime():
    """Scenario with a prime number"""
    assert simple_checking(11) is True

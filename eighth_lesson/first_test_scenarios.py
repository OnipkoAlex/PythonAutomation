import pytest
import to_test


def test_zero():
    assert to_test.some_action(0) == 1


def test_more_than_zero():
    assert to_test.some_action(5) == 120


def test_less_than_zero():
    with pytest.raises(Exception):
        to_test.some_action(-1)

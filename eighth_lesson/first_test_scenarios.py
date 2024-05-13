import pytest
from eighth_lesson import to_test


def test_zero():
    """Scenario with an input number equals to 0"""
    assert to_test.some_action(0) == 1


def test_more_than_zero():
    """Scenario with an input number equals to 5"""
    assert to_test.some_action(5) == 120


def test_less_than_zero():
    """Scenario with an input number less than zero and checking that Exception is raised"""
    with pytest.raises(Exception):
        to_test.some_action(-1)

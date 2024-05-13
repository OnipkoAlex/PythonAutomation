import pytest
from .to_test import some_action


def test_zero():
    """Scenario with an input number equals to 0"""
    assert some_action(0) == 1


def test_more_than_zero():
    """Scenario with an input number equals to 5"""
    assert some_action(5) == 120


def test_less_than_zero():
    """Scenario with an input number less than zero and checking that Exception is raised"""
    with pytest.raises(Exception):
        some_action(-1)

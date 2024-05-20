import pytest
from .to_test import hide_action


@pytest.mark.parametrize("password", ["Abc12!@", "abc12!@3", "Abc12345", "Abc1234~", "AbCd!@%^"])
def test_short_string(password):
    """Scenario with different invalid passwords"""
    assert hide_action(password) is False


def test_valid_string():
    """Scenario with a valid password"""
    assert hide_action("Abc!@#12") is True

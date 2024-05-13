from .to_test import hide_action


def test_short_string():
    """Scenario with short string"""
    assert hide_action("Abc12!@") is False


def test_no_upper_char():
    """Scenario with no upper case letters"""
    assert hide_action("abc12!@3") is False


def test_no_special_char():
    """Scenario with no special symbols"""
    assert hide_action("Abc12345") is False


def test_special_char_not_from_the_list():
    """Scenario with special symbols that are not on the list"""
    assert hide_action("Abc1234~") is False


def test_no_digit():
    """Scenario with no digits"""
    assert hide_action("AbCd!@%^") is False


def test_valid_string():
    """Scenario with a valid string"""
    assert hide_action("Abc!@#12") is True

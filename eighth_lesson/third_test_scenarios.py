from eighth_lesson import to_test


def test_short_string():
    """Scenario with short string"""
    assert to_test.hide_action("Abc12!@") is False


def test_no_upper_char():
    """Scenario with no upper case letters"""
    assert to_test.hide_action("abc12!@3") is False


def test_no_special_char():
    """Scenario with no special symbols"""
    assert to_test.hide_action("Abc12345") is False


def test_special_char_not_from_the_list():
    """Scenario with special symbols that are not on the list"""
    assert to_test.hide_action("Abc1234~") is False


def test_no_digit():
    """Scenario with no digits"""
    assert to_test.hide_action("AbCd!@%^") is False


def test_valid_string():
    """Scenario with a valid string"""
    assert to_test.hide_action("Abc!@#12") is True

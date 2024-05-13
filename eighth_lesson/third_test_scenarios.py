import to_test


def test_short_string():
    assert to_test.hide_action("Abc12!@") is False


def test_no_upper_char():
    assert to_test.hide_action("abc12!@3") is False


def test_no_special_char():
    assert to_test.hide_action("Abc12345") is False


def test_special_char_not_from_the_list():
    assert to_test.hide_action("Abc1234~") is False


def test_no_digit():
    assert to_test.hide_action("AbCd!@%^") is False


def test_valid_string():
    assert to_test.hide_action("Abc!@#12") is True

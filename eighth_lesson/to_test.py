def some_action(n):
    if n < 0:
        raise ValueError("Some error")
    if n == 0:
        return 1
    return n * some_action(n - 1)


def simple_checking(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def hide_action(some_value):
    if len(some_value) < 8:
        return False

    if not any(char.isupper() for char in some_value):
        return False

    special_chars = "!@#$%^&*()-+=_"
    if not any(char in special_chars for char in some_value):
        return False

    if not any(char.isdigit() for char in some_value):
        return False
    return True

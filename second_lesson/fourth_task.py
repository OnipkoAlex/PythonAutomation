def validate(password):
    if len(password) < 8:
        return False

    flag_number = False
    flag_upper = False

    for sym in password:
        if str(sym).isupper():
            flag_upper = True

        if str(sym).isnumeric():
            flag_number = True

    if flag_number and flag_upper:
        return True

    return False


print(validate(input()))

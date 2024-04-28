def count_occurances(string, symbol):
    number = 0

    for sym in string:
        if sym == symbol:
            number += 1

    return number


print(count_occurances(input(), input()))

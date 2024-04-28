def is_palindrome(number):
    if number == number[::-1]:
        return True
    return False


print(is_palindrome(input()))

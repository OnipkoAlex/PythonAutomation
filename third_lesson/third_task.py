def process(*numbers):

    if len(numbers) > 1:
        result = 1

        for num in numbers:
            result *= int(num)

        current = str(result)
    else:
        current = numbers[0]

    result_list = []

    print(current)
    while int(current) > 0:
        result_list.append(int(current[-1:]))
        current = current[:-1]

    return result_list[::-1]


print(process(input()))
# print(process(input(), input(), input()))

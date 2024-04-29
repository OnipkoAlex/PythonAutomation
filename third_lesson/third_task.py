def process(*numbers):
    current = 1

    for num in numbers:
        current *= int(num)

    result_list = []

    print(current)
    while current != 0:
        result_list.append(current % 10)
        current = current // 10

    return result_list[::-1]


print(process(input()))
# print(process(input(), input(), input()))

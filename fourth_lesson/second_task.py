def process(input_list: list):
    return {num: input_list[num - 1] for num in range(1, len(input_list) + 1)}


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(process(a))

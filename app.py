def find_min_max(data):
    min_num = min(data)
    max_num = max(data)
    return (min_num, max_num)


minimum, maximum = find_min_max([1.3, 54, 0.4, 100, 456])
print(minimum, maximum)

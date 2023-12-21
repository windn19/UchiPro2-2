def left_gt(a, b):
    return int(str(a) + str(b)) > int(str(b) + str(a))


def insertion_sort(data):
    for i in range(1, len(data)):
        item_to_insert = data[i]
        j = i
        while j > 0 and left_gt(item_to_insert, data[j - 1]):
            data[j] = data[j - 1]
            j -= 1
        data[j] = item_to_insert
    return data


numbers = list(map(int, input().split()))
result = insertion_sort(numbers)
print(''.join([str(i) for i in result]))



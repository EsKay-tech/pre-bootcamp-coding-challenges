def max(arr):
    max_num = 0

    for i in arr:
        if i >= max_num:
            max_num = i
    return max_num


print(max([-150, -130, 0, -1]))

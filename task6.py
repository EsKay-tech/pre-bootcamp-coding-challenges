def max_num(num_1, num_2, num_3):
    contain = num_1, num_2, num_3
    num = num_1

    for i in contain:
        if i > num:
            num = i
        elif i < -num:
            num = i
        elif i == 0:
            num = i
    return num


print(max_num(-150, 0, -100))

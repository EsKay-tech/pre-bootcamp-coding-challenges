def max_num(num_1, num_2, num_3):
    contain = num_1, num_2, num_3
    num = 0

    for i in contain:
        if i > 0:
            if i > num:
                num = i
            elif i < -num:
                num = i
        else:
            num == 0
    return num


print(max_num(-150, 0, -130))

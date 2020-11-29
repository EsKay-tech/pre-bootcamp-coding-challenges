import re


def three_test(x, y):
    if (x == 3 or y == 3) and re.search("3", str(x+y)):
        return True
    else:
        return False


print(three_test(20, 3))

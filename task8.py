import math


def time(num):
    hours = int(math.floor(num/60))
    minutes = num % 60

    if hours > 1 and minutes > 1:
        print(str(hours) + " hours, " + str(minutes) + " minutes")
    elif hours == 1 and minutes == 1:
        print(str(hours) + " hour, " + str(minutes) + " minute")
    elif hours > 1 and minutes == 1:
        print(str(hours) + " hours, " + str(minutes) + " minute")
    elif hours == 1 and minutes > 1:
        print(str(hours) + " hour, " + str(minutes) + " minutes")
    elif minutes > 1:
        print(str(minutes), 'minutes')
    elif minutes == 1:
        print(str(minutes), 'minute')


time(1)

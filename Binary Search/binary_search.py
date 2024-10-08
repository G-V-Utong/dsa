# Binary search algorithm in python

from math import floor


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    

    while low <= high:
        mid = floor((low + high) / 2)
        guess = list[mid]

        if guess == item :
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

my_list = [1,2,4,6,7,10,12,17,19,21]

print (binary_search(my_list, 10))
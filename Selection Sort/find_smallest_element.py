def findSmallest(arr):
    """This is an example function used to show how selection sort works. This function finds the smallest value in an array"""
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# my_arr = [10, 19, 3, 20, 25, 4, 2, 5, 12]
# findSmallest(my_arr)
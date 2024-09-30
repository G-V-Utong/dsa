from find_smallest_element import findSmallest

def selectionSort(arr):
    new_arr = []

    for i in range(len(arr)):
        entry = findSmallest(arr)
        new_arr.append(arr.pop(entry))
    print(new_arr)


selectionSort([5, 3, 6, 2, 10])
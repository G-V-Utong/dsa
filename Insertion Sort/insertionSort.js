function insertionSort(arr) {
    for (j= 1; j<= arr.length; j++) {
        key = arr[j]
        i = j - 1
        while (i >= 0 && arr[i] > key) {
            arr[i + 1] = arr[i]
            i -= 1
            arr[i + 1] = key
        }
    }
    return arr
}

console.log(insertionSort([10,5,2,4,6,1,3]))
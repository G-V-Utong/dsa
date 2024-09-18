// Binary search in JavaScript

const binarySearch = (list, item) => {
    let low = 0, high = list.length - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let guess = list[mid];

        if (guess === item)
            return mid;
            
        else if (guess < item) 
            low = mid + 1
        else
            high = mid - 1
    }

    return ('The item is not in the list');
}

myList = [1,2,4,6,7,10,12,17,19,21]
let result = binarySearch(myList, 10)
console.log(result)
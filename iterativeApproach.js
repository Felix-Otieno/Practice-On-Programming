
function binarySearch(numbers, x) {
    //@param numbers: an array of integers
    //@param x: a number have to find
    //return: true if number exists else false
    
    let low = 0;
    let high = numbers.length - 1;
    let mid;

    while (low <= high) {
        mid = parseInt(low + (high - low) / 2);

        if (numbers[mid] == x) return true; //Found the number

        else if (x < numbers[mid]) high = mid - 1; //If x is less than the middle element, then the first half of the current search area will be our next search area

        else low = mid + 1; //If x is greater than the middle element, then the last half of the current search area will be our next search area
    }
    return false; //Not found the number
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(binarySearch(numbers, 3)); //Output: false
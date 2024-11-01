function binarySearch(numbers, low, high, x) {
    //@param numbers: an array of integers
    //@param x: a number have to find
    //return: true if number exists else false

    if(low > high) return false; // when not found

    mid = parseInt(low + (high - low) / 2);
    if (numbers[mid] == x) return true; //when found
    else if(x < numbers[mid]) return binarySearch(numbers, low, mid - 1, x); //If x is less than the middle element, then the first half of the current search area will be our next search area
    else return binarySearch(numbers, mid + 1, high, x);  //If x is greater than the middle element, then the last half of the current search area will be our next search area
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(binarySearch(numbers, 0, 9, 11)); //Output: false
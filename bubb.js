function bubbleSort(arr) {
    const n = arr.length;
  
    for (let i = 0; i < n - 1; i++) {
      // <--- Outer loop runs n-1 times (O(n))
      for (let j = 0; j < n - i - 1; j++) {
        // <--- Inner loop runs n-1 times (O(n))
        if (arr[j] > arr[j + 1]) {
          // Swap elements
          [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        }
      }
    }
  
    return arr;
  }
  
  // Example usage:
  const unsortedArray = [64, 34, 25, 12, 22, 11, 90];
  console.log("Unsorted array:", unsortedArray); // [64, 34, 25, 12, 22, 11, 90]
  console.log("Sorted array:", bubbleSort(unsortedArray)); // [11, 12, 22, 25, 34, 64, 90]
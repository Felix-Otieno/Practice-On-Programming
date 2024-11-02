function isPalindrome(str) {
    // Step 1: Normalize the string by converting it to lowercase
    const normalizedStr = str.toLowerCase();
    
    // Step 2: Reverse the string
    const reversedStr = normalizedStr.split('').reverse().join('');
    
    // Step 3: Compare the original normalized string with the reversed string
    return normalizedStr === reversedStr;
}

// Example usage
console.log(isPalindrome("Racecar")); // true
console.log(isPalindrome("Hello")); // false
console.log(isPalindrome("A man, a plan, a canal, Panama")); // false, unless you handle non-alphanumeric characters

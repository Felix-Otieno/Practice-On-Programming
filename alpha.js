function isPalindrome(str) {
    // Normalize: remove non-alphanumeric characters and convert to lowercase
    const normalizedStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    
    // Reverse the string
    const reversedStr = normalizedStr.split('').reverse().join('');
    
    // Compare
    return normalizedStr === reversedStr;
}

// Example usage
console.log(isPalindrome("A man, a plan, a canal, Panama")); // true

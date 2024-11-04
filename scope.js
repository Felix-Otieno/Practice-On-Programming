function outerFunction(outerVariable) {
    function innerFunction() {
        console.log("Outer variable:", outerVariable);
    }
    innerFunction(); // Accessing the outer variable
}

outerFunction("Hello, World!"); // Output: Outer variable: Hello, World!

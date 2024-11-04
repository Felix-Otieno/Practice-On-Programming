function outerFunction(outerVariable) {
    return function innerFunction() {
        console.log("Outer variable:", outerVariable);
    };
}

const innerFunc = outerFunction("Hello, World!");
innerFunc(); // Output: Outer variable: Hello, World!

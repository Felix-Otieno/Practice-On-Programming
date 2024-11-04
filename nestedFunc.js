function outerFunction() {
    console.log("This is outer function.");

    function innerFunction() {
        console.log("This is the inner function.");
    }
    innerFunction(); // Calling the inner function
}
outerFunction(); // Calling the outer function

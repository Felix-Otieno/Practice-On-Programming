let a = 5;
let b = 10;
let c = 2;

let result = a + b * c; // Here, b * c is evaluated first due to higher precedence.
console.log(result); // Outputs: 25

let value = 10 - 5 + 3; // Evaluated left-to-right.
console.log(value); // Outputs: 8

let exponent = 2 ** 3 ** 2; // Right-to-left associativity.
console.log(exponent); // Outputs: 512 (2 ** 9)

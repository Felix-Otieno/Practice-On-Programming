let numbers = [45, 56, 78, 999, 125, 67, 900, 123, 56];

let maximum = numbers[0];

for(let i = 0; i < numbers.length; i++ ) {
    
    let current = numbers[i];

    if (current > maximum) {
        maximum = current;

    }
}
console.log(maximum);
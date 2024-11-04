// Sample array of objects
const people = [
    { name: 'Alice', age: 25 },
    { name: 'Bob', age: 20 },
    { name: 'Charlie', age: 30 }
];

// Sorting by age
people.sort((a, b) => a.age - b.age);

console.log(people);

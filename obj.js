let person = {
    name: "Alice",
    age: 38,
    tribe: "luo",
    nationality: "Kenyan",
    resident: "Jenga"
}

for(key, value in person.items()) {
    console.log(person[key], ":", value);
}

console.log(person);
console.log(person.name);
console.log(typeof(person));

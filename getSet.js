// get it is a function that is called to retrieve the value of the property while set it is a function that is called when a property has been assign a value.

let person = {
    name: "John",
    surname: "Doe"
}

Object.defineProperty(person, "fullName", {
    get: function() {
        return this.name + " " + this.surname;
    },
    set: function(value) {
        [this.name, this.surname] = value.split(" ");
    }
});

console.log(person.fullName);

person.surname = "Hill"
console.log(person.fullName);

person.fullName = "Mary Jones";
console.log(person.fullName);
console.log(person.name);
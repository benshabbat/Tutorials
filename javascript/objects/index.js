
// object = A collection of related properties and/or methods
//                Can represent real world objects (people, products, places)
//                object = {key:value,
//                               function()}

const person1 = {
    firstName: "DavidChen",
    lastName: "Benshabbat",
    age: 30,
    isEmployed: true,
    sayHello: function(){console.log(`Hi! I am ${this.firstName}!`)},
    eat: function(){console.log("I am eating a vegetables")},
}

const person2 = {
    firstName: "Miriam",
    lastName: "Benshabbat",
    age: 42,
    isEmployed: false,
    sayHello: () => console.log(`Hey, I'm Miriam`),
    eat: () => console.log("I am eating pizza"),
}

console.log(person1.firstName);
console.log(person2.firstName);

person1.sayHello();
person1.eat();
person2.sayHello();
person2.eat();
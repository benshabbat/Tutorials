// nested objects = Objects inside of other Objects.
//                               Allows you to represent more complex data structures
//                               Child Object is enclosed by a Parent Object

//                               Person{Address{}, ContactInfo{}}
//                               ShoppingCart{Keyboard{}, Mouse{}, Monitor{}}

class Person {
  constructor(name, age, ...address) {
    this.name = name;
    this.age = age;
    this.address = new Address(...address);
  }
}

class Address {
  constructor(street, city, country) {
    this.street = street;
    this.city = city;
    this.country = country;
  }
}

const address1 = new Address("124 Conch St.", "Bikini Bottom", "Int. Waters");
//not good
const person1 = new Person("Spongebob", 30, address1);

const address2 = new Address("128 Conch St.", "Bikini Bottom", "Int. Waters");
//not good
const person2 = new Person("Patrick", 37, address2);

const address3 = new Address("126 Conch St.", "Bikini Bottom", "Int. Waters");
const person3 = new Person("Squidward", 45, "126 Conch St.", "Bikini Bottom", "Int. Waters");

console.log(person1.name);
console.log(person1.age);
console.log(person3.address);
console.log(person3.address.street);
console.log(person3.address.city);
console.log(person3.address.country);
console.log(address3)
console.log(address3.street)

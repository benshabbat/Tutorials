// inheritance = allows a new class to inherit properties and methods
//                         from an existing class (parent -> child)
//                         helps with code reusability

class Animal {
  alive = true;

  eat() {
    console.log(`This ${this.name} is eating`);
  }
  sleep() {
    console.log(`This ${this.name} is sleeping`);
  }
}


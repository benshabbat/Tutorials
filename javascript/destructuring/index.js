// destructuring =  extract values from arrays and objects,
//                              then assign them to variables in a convenient way
//                              [] = to perform array destructuring
//                              {} = to perform object destructuring

// ---------- EXAMPLE 1 ----------
// SWAP THE VALUE OF TWO VARIABLES

let a = 1;
let b = 2;

console.log("Before Destructure A:" + a);
console.log("Before Destructure B:" + b);
[a, b] = [b, a];

console.log("After Destructure A:" + a);
console.log("After Destructure B:" + b);

// ---------- EXAMPLE 2 ----------
// SWAP 2 ELEMENTS IN AN ARRAY

const colors = ["red", "green", "blue", "black", "white"];
console.log("Before Destructure :" + colors);

[colors[0], colors[4]] = [colors[4], colors[0]];

console.log("After Destructure :" + colors);

// ---------- EXAMPLE 3 ----------
// ASSIGN ARRAY ELEMENTS TO VARIABLES

const [firstColor, secondColor, thirdColor, ...extraColors] = colors;

console.log(firstColor);
console.log(secondColor);
console.log(thirdColor);
console.log(extraColors);

const colors2 = [firstColor, secondColor, thirdColor, ...extraColors];
console.log(colors2);

// ---------- EXAMPLE 4 ----------
// EXTRACT VALUES FROM OBJECTS

const person1 = {
  firstName: "DavidChen",
  lastName: "Benshabbat",
  age: 30,
  job: "Software Developer",
};

const person2 = {
  firstName: "Miriam",
  lastName: "Benshabbat",
  age: 28,
  job: "Officer",
};
const person3 = {
  firstName: "Avishag",
  lastName: "Benshabbat",
  age: 2,
};

const { firstName, lastName, age, job = "Unemployed" } = person3;

console.log(firstName);
console.log(lastName);
console.log(age);

// ---------- EXAMPLE 5 ----------
// DESTRUCTURING IN FUNCTION PARAMETERS

function displayPerson({ firstName, lastName, age, job="Unemployed" }) {
    console.log(`name: ${firstName} ${lastName}`);
    console.log(`age: ${age}`);
    console.log(`job: ${job}`);
}

displayPerson(person1);
displayPerson(person2);
displayPerson(person3);
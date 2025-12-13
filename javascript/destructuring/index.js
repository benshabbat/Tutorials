// destructuring =  extract values from arrays and objects,
//                              then assign them to variables in a convenient way
//                              [] = to perform array destructuring
//                              {} = to perform object destructuring

// ---------- EXAMPLE 1 ----------
// SWAP THE VALUE OF TWO VARIABLES

// let a = 1;
// let b = 2;
// console.log("Before Destructure A:" + a);
// console.log("Before Destructure B:" + b);
// [a, b] = [b, a];
// console.log("After Destructure A:" + a);
// console.log("After Destructure B:" + b);

// // ---------- EXAMPLE 2 ----------
// // SWAP 2 ELEMENTS IN AN ARRAY

// console.log("Before Destructure :" + colors);
// [colors[0], colors[4]] = [colors[4], colors[0]];
// console.log("After Destructure :" + colors);

// // ---------- EXAMPLE 3 ----------
// // ASSIGN ARRAY ELEMENTS TO VARIABLES

const colors = ["red", "green", "blue", "black", "white"];
const [firstColor, secondColor, thirdColor,...extraColors] = colors;
// const [firstColor] = colors;
// console.log(...colors)
// console.log(firstColor);
// console.log(firstColor.toUpperCase())
// console.log(colors)

// console.log(secondColor);
// console.log(thirdColor);
// console.log(extraColors);

// const colors2 = [firstColor, secondColor, thirdColor, ...extraColors];
// console.log(colors2);

// // ---------- EXAMPLE 4 ----------
// // EXTRACT VALUES FROM OBJECTS

// const person1 = {
//   firstName: "David-Chen",
//   lastName: "Benshabbat",
//   age: 30,
//   job: "Software Developer",
// };

// const person2 = {
//   firstName: "Miriam",
//   lastName: "Benshabbat",
//   age: 29,
//   job: "Officer",
// };
// const person3 = {
//   firstName: "Avishag",
//   lastName: "Benshabbat",
//   age: 4,
// };

// console.log({...person3})
// const person5 = {...person3 }
// console.log(person5)
// console.log({...person5})
// console.log(person3)
// person3.job = job
// const { job } = person3;
// console.log(job)
// console.log(person3)
// const person4 = {
//   firstName: "Nehoray-Izhack",
//   lastName: "Benshabbat",
//   age: 1,
// };

// 
// console.log(firstName);
// console.log(lastName);
// console.log(age);

// // ---------- EXAMPLE 5 ----------
// // DESTRUCTURING IN FUNCTION PARAMETERS

// function displayPerson({ firstName, lastName, age, job="Unemployed" }) {
//     console.log(`name: ${firstName} ${lastName}`);
//     console.log(`age: ${age}`);
//     console.log(`job: ${job}`);
// }

// displayPerson(person1);
// displayPerson(person2);
// displayPerson(person3);
// displayPerson(person4);


const users = [
  { name: "Alice", age: 28 },
  { name: "Bob", age: 34 },
  { name: "Charlie", age: 22 },
];



// const users2 = [users.map(user=>user)
// users2[0].age = 22
// console.log(users)
// console.log(users2)
// const [user1,user2,user3] = users;
// const {name: name1} = user1;
// const {name: name2, age: age2} = user2;

// const numbers = [1, 2, 3];

// // console.log(...numbers)
// const numbers2 = [...numbers]
// numbers2[0] = 99
// console.log(numbers)
// console.log(numbers2)
// Example 1
// This demonstrates how destructuring can be used to swap values without a temporary variable
let a = 1;
let b = 2;
console.log(a); 
console.log(b);
[a, b] = [b, a];
console.log(a);
console.log(b);

// Example 2
// This shows how to use destructuring to swap elements within an array

const colors = ["red", "green", "blue", "black", "white"];
console.log(colors);

// Swap first and last elements using destructuring
[colors[0], colors[4]] = [colors[4], colors[0]];
console.log(colors);

// Example 3
// This demonstrates array destructuring and the rest operator
const [firstColor, secondColor, thirdColor, ...extraColors] = colors;
console.log(firstColor);
console.log(secondColor);
console.log(thirdColor);
console.log(extraColors);

// Create a new array using destructured variables and the spread operator
const colors2 = [secondColor, firstColor, thirdColor, ...extraColors];
console.log(colors2);

// Example 4
// This shows object destructuring with default values
const person1 = { firstName: "Joseph", lastName: "Cohen", age: 35, occupation: "Teacher" };
const person2 = { firstName: "Rachel", lastName: "Levy", age: 28, occupation: "Doctor" };
const person3 = { firstName: "Daniel", lastName: "Goldstein", age: 5 };
// Destructure person3 object with a default value for 'occupation'
const { firstName, lastName, age, occupation = "Unemployed" } = person3;

console.log(firstName);
console.log(lastName);
console.log(age);
console.log(occupation);

// Example 5
// This demonstrates how to use destructuring in function parameters

// Create an array of person objects
const persons = [person1, person2, person3];

function displayPerson({ firstName, lastName, age, occupation = "Unemployed" }) {
  console.log(`name: ${firstName} ${lastName}`);
  console.log(`age: ${age}`);
  console.log(`occupation: ${occupation}`);
}

// Use forEach to call displayPerson for each person in the persons array
persons.forEach((person) => displayPerson(person));

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


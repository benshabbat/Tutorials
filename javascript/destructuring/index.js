// destructuring =  extract values from arrays and objects,
//                              then assign them to variables in a convenient way
//                              [] = to perform array destructuring
//                              {} = to perform object destructuring

// ---------- EXAMPLE 1 ----------
// SWAP THE VALUE OF TWO VARIABLES

let a = 1;
let b = 2;

console.log("Before Destructure A:"+a);
console.log("Before Destructure B:"+b);
[a, b] = [b, a];

console.log("After Destructure A:"+a);
console.log("After Destructure B:"+b);


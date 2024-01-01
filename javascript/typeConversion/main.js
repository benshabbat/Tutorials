// type conversion = change the datatype of a value to another
//                                 (strings, numbers, booleans)

// --------------- EXAMPLE 1 ---------------
let age = window.prompt("How old are you?");
age = Number(age);
age+=1;

console.log(age, typeof age);

// --------------- EXAMPLE 2 ---------------
let x = "david";
let y = "david";
let z = "david";

x = Number(x);
y = String(y);
z = Boolean(z);

console.log(x, typeof x);
console.log(y, typeof y);
console.log(z, typeof z);
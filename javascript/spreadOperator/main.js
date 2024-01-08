// spread operator =  ... allows an iterable such as an
//                                  array or string to be expanded
//                                   in to separate elements
//                                  (unpacks the elements)

// ------------ EXAMPLE 1 ------------
//unpacks the elements
let numbers = [1, 2, 3, 4, 5];
let maximum = Math.max(...numbers);
let minimum = Math.min(...numbers);

console.log(maximum);

// ------------ EXAMPLE 2 ------------
//array of characters
let username = "Bro Code";
let letters = [...username]; 

console.log(letters);

// ------------ EXAMPLE 3 ------------
let fruits = ["apple", "orange", "banana"];
let vegetables = ["carrots", "celery", "potatoes"];
//combine two arrays
let foods = [...fruits, ...vegetables, "eggs", "milk"];

console.log(foods);
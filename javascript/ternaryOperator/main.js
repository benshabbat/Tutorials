// ternary operator = a shortcut to if{} and else{} statements
//                                  helps to assign a variable based on a condition
//                                  condition ? codeIfTrue : codeIfFalse;

// Example 1
let time = 9;
let greeting = time < 12 ? "Good morning!" : "Good afternoon!";
console.log(greeting);

// Example 2
let isStudent = false;
let message = isStudent ? "You are a student" : "You are NOT a student";
console.log(message);

// Example 3
let purchaseAmount = 99;
let discount = purchaseAmount >= 100 ? 10 : 0;
console.log(`Your total is $${purchaseAmount - purchaseAmount * (discount/100)}`);
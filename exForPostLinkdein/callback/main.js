

const sum = (callback, num1, num2) => callback(num1 + num2);

// Example 1: Using function return values
// In this case, num1() and num2() are invoked, returning 4 and 5.
// The 'print' function is passed as a callback.
// This will correctly log 9 (4 + 5).
const num1 = () => 4;
const num2 = () => 5;
const print = (res) => console.log(res);
sum(print, num1(), num2());

// Example 2: Using direct values
// Here, num3 and num4 are already values (4 and 5).
// 'print2' is passed as a callback.
// This will also correctly log 9 (4 + 5).
const num3 = 4;
const num4 = 5;
const print2 = (res) => console.log(res);
sum(print2, num3, num4);

// Example 3: Incorrect usage - invoking the callback
// This example demonstrates a common mistake.
// print3() is invoked immediately, not passed as a callback.
// This will cause an error because undefined is passed as the callback.
const num5 = 4;
const num6 = 5;
const print3 = (res) => console.log(res);
sum(print3(), num5, num6);  // This will throw an error

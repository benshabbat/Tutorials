//Rest Parameters (...args)
//EXAMPLE 1
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}
console.log(sum(1, 2, 3, 4)); 
//EXAMPLE 2
function getAverage(...numbers) {
    return numbers.reduce((total, num) => total + num, 0) / numbers.length;
}
console.log(getAverage(1, 2, 3, 4)); 

//Spread Operator (...)
//EXAMPLE 1
//unpacks the elements
let numbers = [1, 2, 3, 4, 5];
let maximum = Math.max(...numbers);
let minimum = Math.min(...numbers);
console.log(maximum);
console.log(minimum);

//EXAMPLE 2
//combine two arrays
const arr1 = [1, 2, 3];
const arr2 = [4, 5];
const arr3 = [...arr1,...arr2,5,6];
console.log(arr3); 

//EXAMPLE 3
//array of characters
let username = "Benshabbat";
let letters = [...username]; 
console.log(letters);
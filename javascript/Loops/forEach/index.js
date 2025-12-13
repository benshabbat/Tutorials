// // forEach() = method used to iterate over the elements
// //                     of an array and apply a specified function (callback)
// //                     to each element

// //                     array.forEach(callback)
// //                     element, index, array are provided

// // ------------- EXAMPLE 1 -------------

// // numbers.forEach(cube);
// // numbers.forEach(display);

// //how working forEach function
function double(element, index, array){
    array[index] = element * 2;
}
const numbers = [1, 2, 3, 4, 5];
const numbers2 = numbers.map((num)=> num+10)
console.log("numbers2",numbers2)
console.log("numbers", numbers)
numbers.forEach(double);
// console.log(numbers);
// numbers.forEach(double);
// console.log(numbers);

// function triple(element, index, array){
//     array[index] = element * 3;
// }
// numbers.forEach((number)=>{
//     console.log(number*3)
// })

// function square(element, index, array){
//     array[index] = Math.pow(element, 2);
// }
// numbers.forEach((number)=>{
//     console.log(Math.pow(number, 2))
// })

// function cube(element, index, array){
//     array[index] = Math.pow(element, 3);
// }
// numbers.forEach((number)=>{
//     console.log(Math.pow(number, 3))
// })

// function display(element){
//     console.log(element);
// }

// // ------------- EXAMPLE 2 -------------

// let fruits = ["apple", "orange", "banana", "coconut"];

// // fruits.forEach(capitalize);
// // fruits.forEach(display);

// function upperCase(element, index, array){
//     array[index] = element.toUpperCase();
// }
// fruits.forEach((food)=>{
//     console.log(food.toUpperCase())
// })

// function lowercase(element, index, array){
//     array[index] = element.toLowerCase();
// }
// fruits.forEach((food)=>{
//     console.log(food.toLowerCase())
// })

// function capitalize(element, index, array){
//     array[index] = element.charAt(0).toUpperCase() + element.slice(1).toLowerCase();
// }

// fruits.forEach((food)=>{
//     console.log(food.charAt(0).toUpperCase() + food.slice(1).toLowerCase())
// })

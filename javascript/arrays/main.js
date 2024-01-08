// array = a variable like structure that can 
//             hold more than 1 value

let fruits = ["apple", "orange", "banana", "coconut"];

fruits.push("coconut");  //add an element
fruits.pop();                     //removes last element
fruits.unshift("mango"); //add element to beginning
fruits.shift();                    //removes element from beginning

let numOfFruits = fruits.length;
let index = fruits.indexOf("coconut");

console.log(fruits);
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);
console.log(fruits[3]);

console.log(numOfFruits);
console.log(index);


for(let i = 0; i < fruits.length; i++){
    console.log(fruits[i]);
}


for(let i = fruits.length - 1; i >= 0; i--){
    console.log(fruits[i]);
}


fruits.sort();
fruits.sort().reverse();
//short cut for
for(let fruit of fruits){
    console.log(fruit);
}
// filter() = creates a new array by filtering out
//                elements with a callback

// ----------- EXAMPLE 1 -----------
let numbers = [1, 2, 3, 4, 5, 6, 7];
let evenNums = numbers.filter(isEven);
let oddNums = numbers.filter(isOdd);

console.log(oddNums);

function isEven(element){
    return element % 2 === 0;
}

function isOdd(element){
    return element % 2 !== 0;
}
// ----------- EXAMPLE 2 -----------
let ages = [16, 17, 17, 18, 19, 20, 65];
let adults = ages.filter(isAdult);
let children = ages.filter(isChild);

console.log(children);

function isAdult(element){
    return element >= 18;
}

function isChild(element){
    return element < 18;
}


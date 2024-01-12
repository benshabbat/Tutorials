// forEach() = method used to iterate over the elements 
//                     of an array and apply a specified function (callback)
//                     to each element

//                     array.forEach(callback)
//                     element, index, array are provided

// ------------- EXAMPLE 1 -------------

const numbers = [1, 2, 3, 4, 5];

// numbers.forEach(cube);
// numbers.forEach(display);

function double(element, index, array){
    array[index] = element * 2;
}
numbers.forEach((number)=>{
    console.log(number*2)
})



function display(element){
    console.log(element);
}


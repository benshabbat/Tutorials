function sum(...rest) {
  console.log(rest);
  let sum = 0;
  for (let i = 0; i < rest.length; i++) {
    sum += rest[i];
  }
  return sum;
}
const arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const arr2 = [ 1, 3,6,7,8,9]
const arr3 = [...arr,...arr2]
// const arr4 = [...arr]
const arr4 = arr
arr4[5]= 9
console.log(arr4)
console.log(arr)
// console.log(arr4===arr)
// console.log(...arr)
// console.log(sum(1, 2, 3, 4, 5));
// console.log(sum(...arr));

// rest parameters = (...rest) allow a function work with a variable
//                                  number of arguments by bundling them into an array

//                                  spread = expands an array into separate elements
//                                  rest = bundles separate elements into an array

// ------- EXAMPLE 1 -------
function openFridgeArr(...foods) {
  console.log(foods);
}
function openFridge(...foods) {
  console.log(...foods);
}
function getFood(...foods) {
  return foods;
}

const food1 = "pizza";
const food2 = "hamburger";
const food3 = "hotdog";
const food4 = "sushi";

openFridge(food1, food2, food3, food4);

const foods = getFood(food1, food2, food3, food4);

// ------- EXAMPLE 2 -------
function sum(...numbers) {
  let result = 0;
  for (let number of numbers) {
    result += number;
  }
  return result;
}

function getAverage(...numbers) {
  let result = 0;
  for (let number of numbers) {
    result += number;
  }
  return result / numbers.length;
}

const average = getAverage(75, 100, 85, 90, 50);

console.log(average);

// ------- EXAMPLE 3 -------
function combineStrings(...strings) {
  return strings.join(" ");
}
function combineStringsToArray(...strings) {
  return strings;
}

const fullName = combineStrings("Mr.", "Spongebob", "Squarepants", "III");
const arr = combineStringsToArray("Mr.", "Spongebob", "Squarepants", "III");

console.log(fullName);
console.log(arr);

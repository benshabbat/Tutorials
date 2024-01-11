// callback = a function that is passed as an argument
//                    to another function.

//                    used to handle asynchronous operations:
//                    1. Reading a file
//                    2. Network requests
//                    3. Interacting with databases

//                    "Hey, when you're done, call this next."

function sum(callback, num1, num2) {
  callback(num1 + num2);
}

function print(res) {
  document.getElementById("res").textContent = res;
}
//static working
// sum(print,4,4);

// dynamic working
function calculate() {
  const num1 = document.getElementById("num1").value;
  const num2 = document.getElementById("num2").value;
  sum(print, Number(num1), Number(num2));
}

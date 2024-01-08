// function = A section of reusable code.
//                    Declare code once, use it whenever you want.
//                    Call the function to execute that code.


//include parameters
function happyBirthday(username, age){
  console.log(`Happy birthday to you!`);
  console.log(`Happy birthday to you!`);
  console.log(`Happy birthday dear, ${username}`);
  console.log(`Happy birthday to you!`);
  console.log(`You are ${age} years old!`);
}
//set arguments
console.log(happyBirthday("David", 30));

//ex add
function add(x, y){
  return x + y;
}

//ex subtract
function subtract(x, y){
  return x - y;
}

//ex multiply
function multiply(x, y){
  return x * y;
}

//ex divide
function divide(x, y){
  return x / y;
}

//ex if is even
function isEven(number){

  return number % 2 === 0 ? true : false;
}

//ex valid on email
function isValidEmail(email){

  return email.includes("@") ? true : false;
}

console.log(isValidEmail("David@gmail.com"));
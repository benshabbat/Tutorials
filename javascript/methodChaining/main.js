
// Method Chaining = Calling one method after another
//                                    in one continuous line of code.

let username = window.prompt("Enter your username: ");

// ---- NO METHOD CHAINING ----

username = username.trim();
let letter = username.charAt(0);
letter = letter.toUpperCase();

let extraChars = username.slice(1);
extraChars = extraChars.toLowerCase();
username = letter + extraChars;

console.log(username);



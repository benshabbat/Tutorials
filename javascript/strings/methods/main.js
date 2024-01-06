// string methods = allow you to manipulate and work with text (strings)

let userName = "DavidChen Benshabbat";
let phoneNumber = "123-456-7890";

console.log(userName.length);
console.log(userName.charAt(0));
console.log(userName.indexOf("a"));
console.log(userName.lastIndexOf("a"));
userName = userName.trim();
userName = userName.toUpperCase();
userName = userName.toLowerCase();
userName = userName.repeat(3);
// let result = userName.startsWith(" ");
// let result = userName.endsWith(" ");
let result = userName.includes(" ");
phoneNumber = phoneNumber.replaceAll("-", "");
phoneNumber = phoneNumber.padStart(15, "0");
phoneNumber = phoneNumber.padEnd(15, "0");

console.log(phoneNumber);
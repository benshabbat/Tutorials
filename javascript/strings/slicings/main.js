// string slicing = creating a substring
//                            from a portion of another string
//                            string.slice(start, end)

// Example 1

const fullName = "DavidChen Benshabat";
const firstName = fullName.slice(0, fullName.indexOf(" "));
const lastName = fullName.slice(fullName.indexOf(" ") + 1);
console.log(firstName);
console.log(lastName);

// Example 2

const email = "Benshabbat27@gmail.com";
const userName = email.slice(0,email.indexOf("@"));
const extension = email.slice(email.indexOf("@") + 1);
console.log(userName);
console.log(extension);

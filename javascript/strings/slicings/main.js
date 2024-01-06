// string slicing = creating a substring
//                            from a portion of another string
//                            string.slice(start, end)

// Example 1

const fullName = "DavidChen Benshabat";
const firstName = fullName.slice(0, fullName.indexOf(" "));
const lastName = fullName.slice(fullName.indexOf(" ") + 1);
console.log(firstName);
console.log(lastName);

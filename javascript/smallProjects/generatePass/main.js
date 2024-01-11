// RANDOM PASSWORD GENERATOR

function generatePassword(length,includeLowercase,includeUppercase,includeNumbers,includeSymbols) {
  const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
  const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const numberChars = "0123456789";
  const symbolChars = "!@#$%^&*()_+-=";

  let allowedChars = "";
  let password = "";

  //if is true concatenates to allow characters
  allowedChars += includeLowercase ? lowercaseChars : "";
  allowedChars += includeUppercase ? uppercaseChars : "";
  allowedChars += includeNumbers ? numberChars : "";
  allowedChars += includeSymbols ? symbolChars : "";

  if (length <= 0) {
    return `(password length must be at least 1)`;
  }
  // randomly generate if the user does not choose any options to be allowed
  if (allowedChars.length === 0) {
    allowedChars += lowercaseChars
    allowedChars += uppercaseChars
    allowedChars += numberChars
    allowedChars += symbolChars
  }

  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * allowedChars.length);
    password += allowedChars[randomIndex];
  }

  return password;
}

const passwordLength = 10;
const includeLowercase = false;
const includeUppercase = false;
const includeNumbers = false;
const includeSymbols = false;

const password = generatePassword(passwordLength,includeLowercase,includeUppercase,includeNumbers,includeSymbols);

console.log(`Generated password: ${password}`);

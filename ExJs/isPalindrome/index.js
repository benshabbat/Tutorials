// הקוד הבא אמור לבדוק אם מחרוזת היא פלינדרום (נקראת אותו דבר מימין לשמאל ומשמאל לימין)
// אבל יש בו באג. מצא ותקן את הבאג

const str = "level";
function isPalindrome(str) {
  str = str.toLowerCase();
  let reversedStr = "";

  for (let i = 0; i < str.length; i++) {
    reversedStr = str[i] + reversedStr;
  }

  return (str = reversedStr);
}

function isPalindromeFix(str) {
  let reversedStr = "";

  for (let i = 0; i < str.length; i++) {
    reversedStr += str[(str.length-1) - i];
  }

  return (str === reversedStr);
}


console.log(isPalindrome(str));
console.log(isPalindromeFix(str));

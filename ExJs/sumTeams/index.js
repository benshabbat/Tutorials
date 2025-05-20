// כתוב פונקציה שמקבלת מערך מספרים ומחזירה את הסכום של כל המספרים החיוביים במערך
function sumPositiveNumbers(arr) {
  return arr.reduce((acc, num) => {
    if (num > 0) {
      return acc + num;
    }
    return acc; // החזר את הערך המצטבר אם המספר אינו חיובי
  }, 0); // אתחל את הערך המצטבר ל-0
}

console.log(sumPositiveNumbers([1, -2, 3, -4, 5])); // 9
// לדוגמה: sumPositiveNumbers([1, -2, 3, -4, 5]) צריך להחזיר 9

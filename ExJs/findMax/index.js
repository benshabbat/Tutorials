// הקוד הבא אמור להחזיר את המספר הגדול ביותר במערך
// אך יש בו באג. מצא ותקן את הבאג

function findMax(numbers) {
  let max = 0;
  
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
  }
  
  return max;
}
// הפונקציה אמורה להחזיר 5 עבור [1, 3, 5, 2, 4]
// ו-10 עבור [-5, 0, 10, -2]
console.log(findMax([1, 3, 5, 2, 4])); // 5
console.log(findMax([-5, 0, 10, -2])); // 10

function findMaxFix(numbers) {
  let max = numbers.length>0 ? numbers[0] : -Infinity;
  // אם המערך ריק, מחזירים -Infinity
  // אם המערך לא ריק, מחזירים את המספר הראשון במערך
  // וממשיכים לבדוק את שאר המספרים במערך
  
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
  }
  
  return max;
}
function findMax(numbers) {
  return numbers.length > 0 ? Math.max(...numbers) : -Infinity;
}

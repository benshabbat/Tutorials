// פתרון 1: שימוש בסט (Set) - פתרון יעיל וקריא
function hasUniqueChars(str) {
    // אם גודל הסט שווה לאורך המחרוזת, אז כל התווים ייחודיים
    return new Set(str).size === str.length;
  }
  
  // פתרון 2: שימוש באובייקט לעקוב אחר תווים שכבר ראינו
  function hasUniqueCharsUsingObject(str) {
    const charsSeen = {};
    
    for (let char of str) {
      // אם כבר ראינו את התו, המחרוזת אינה מכילה רק תווים ייחודיים
      if (charsSeen[char]) {
        return false;
      }
      // סימון שראינו את התו
      charsSeen[char] = true;
    }
    
    // אם הגענו לכאן, כל התווים ייחודיים
    return true;
  }
  
  // פתרון 3: גישה ברוטלית, השוואת כל זוג תווים (יעילות פחותה)
  function hasUniqueCharsNested(str) {
    for (let i = 0; i < str.length; i++) {
      for (let j = i + 1; j < str.length; j++) {
        if (str[i] === str[j]) {
          return false;
        }
      }
    }
    return true;
  }
  
  // דוגמאות שימוש:
  console.log(hasUniqueChars("abcde"));     // true
  console.log(hasUniqueChars("hello"));     // false
  console.log(hasUniqueChars("123456"));    // true
  console.log(hasUniqueChars("1234561"));   // false
const mySet = new Set();

// הוספת ערכים
mySet.add(1);
mySet.add("text");
mySet.add({name: "John"});

// ניסיון להוסיף ערך קיים לא ישנה את הסט
mySet.add(1);
console.log(mySet); 
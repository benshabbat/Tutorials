const fruits = [
  { name: "apple", color: "red", calories: 95 },
  { name: "orange", color: "orange", calories: 45 },
  { name: "banana", color: "yellow", calories: 105 },
  { name: "coconut", color: "white", calories: 159 },
  { name: "pineapple", color: "yellow", calories: 37 },
];

// Access properties of a fruit object
console.log(fruits[0].calories);

// Add a new fruit object
fruits.push({ name: "grapes", color: "purple", calories: 62 });

// Remove the last fruit object
fruits.pop();
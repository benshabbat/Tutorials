const data = [
  {
    name: "John",
    birthday: "1-1-1995",
    favoriteFoods: {
      meats: ["hamburgers", "sausages"],
      fish: ["salmon", "pike"],
    },
  },
  {
    name: "Mark",
    birthday: "10-5-1980",
    favoriteFoods: {
      meats: ["hamburgers", "steak", "lamb"],
      fish: ["tuna", "salmon", "barracuda"],
    },
  },
  {
    name: "Mary",
    birthday: "1-10-1977",
    favoriteFoods: {
      meats: ["cow", "chicken"],
      fish: ["pike"],
    },
  },
  {
    name: "Thomas",
    birthday: "1-10-1990",
    favoriteFoods: {
      meats: ["bird", "rooster"],
      fish: ["salmon"],
    },
  },
  {
    name: "Mary",
    birthday: "1-10-1977",
    favoriteFoods: {
      meats: ["hamburgers", "lamb"],
      fish: ["bass", "tuna"],
    },
  },
];

// function countAllFoods(people) {
//   const foodCount = {};
  
//   people.forEach(person => {
//     const { favoriteFoods } = person;
    
//     // Iterate through all food categories (meats, fish, etc.)
//     Object.values(favoriteFoods).forEach(foodArray => {
//       foodArray.forEach(food => {
//         foodCount[food] = (foodCount[food] || 0) + 1;
//       });
//     });
//   });
  
//   return foodCount;
// }

// const result = countAllFoods(data);
// console.log(result);


function countAllFoods(people) {
  const foodCount = {};
  
  people.forEach(person => {
    const { meats, fish } = person.favoriteFoods;
    
    meats.forEach(food => {
      foodCount[food] = (foodCount[food] || 0) + 1;
    });
    
    fish.forEach(food => {
      foodCount[food] = (foodCount[food] || 0) + 1;
    });
  });
  
  return foodCount;
}

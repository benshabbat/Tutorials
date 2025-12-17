// Promise-based Refactor Example


// const cbPromise = (resolve, reject) => {
//   if (true) {
//     resolve("Success!");
//   } else {
//     reject("Failure!");
//   }
// };

function checkEven(num) {
  return new Promise(((resolve, reject) => {
    if (num % 2 === 0) {
      resolve(num*5);
    } else {
      reject("IS ODD !");
    }
  }));
}
checkEven(4).then(msg => {
  console.log(msg);
}).catch(err => {
  console.log(err);
});


// const pathUsers = "https://jsonplaceholder.typicode.com/users"

// function getUsers(url) {

//   return fetch(url).then(response => response.json());
// }

// getUsers(pathUsers).then(users => {
//   console.log(users);
// }).catch(err => {
//   console.log(err);
// });
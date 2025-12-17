// const url = "https://swapi.dev/api/";
// const url2 = "https://jsonplaceholder.typicode.com/";

// async function fetchData() {
//   try {
//     const response = await fetch(url);
//     const data = await response.json();
//     return data;
//   } catch (error) {
//     return "Error fetching data:" + error.message;
//   }
// }

// const data = await fetchData()
// console.log(data)

// const keys = Object.keys(data);
// console.log(keys);

// async function fetchDataFromArr(path) {
//   try {
//     const response = await fetch(url+path);
//     const data = await response.json();
//     return data;
//   } catch (error) {
//     return "Error fetching data:" + error.message;
//   }
// }

// const data2 = await fetchDataFromArr(keys[0])
// console.log(data2)

// TODO: השלם את הפונקציה
async function getUser(userId) {
  try {
    const response = await fetch(
      `https://jsonplaceholder.typicode.com/users/${userId}`
    );
    // console.log(response);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status} ${response.statusText}`);
    }
    const user = await response.json();
    return user;


  } catch (error) {
    console.error("Error fetching user data:", error);
    return null; // או תוכל להחזיר ערך אחר שמציין שגיאה
  }
}

// getUser(1)

getUser(1).then(user => console.log(user.name)); // צריך להדפיס: Leanne Graham
getUser(999).then(user => console.log(user)); // צריך להדפיס: null או להציג שגיאה

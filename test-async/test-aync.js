import fs from "fs/promises";
import { findPepoleByType, getDataAndCreateJsonFile } from "./utils.js";

const url = "https://spies-test-server.vercel.app/";
async function getPeopleList() {
  const response = await fetch(`${url}/people`);
  const peopleArray = await response.json();
  await fs.writeFile("./test-async/data/PEOPLE.json", JSON.stringify(peopleArray));
  return peopleArray;
}
console.log(await getDataAndCreateJsonFile('people') );
// console.log(await getPeopleList() );

// 2. Get Call Records/Transcriptions
// Send a request to the intelligence server  - general url + “/transcriptions”
// Receive an array of call record objects.
// Save only the array into a file named TRANSCRIPTIONS.json.

// async function getCallRecords() {
//     const response = await fetch(`${url}/transcriptions`);
//     const callRecordsArray = await response.text();
//     await fs.writeFile('./test-async/data/TRANSCRIPTIONS.json', callRecordsArray);
//     return callRecordsArray;
// }
// console.log(await getCallRecords() );

// console.log(await getDataAndCreateJsonFile('transcriptions') );

//   Search People by Name
// Load the people list from the file. Use the fs module - callback or promises.
// Convert the text into JSON using JSON.parse (if needed)
// Ask the user to enter a name.
// Search for the person:
// If found – print the person object.
// If not found – print a message saying the person was not found.

// async function findPersonByName(name) {
//   const peopleData = await fs.readFile('./test-async/data/PEOPLE.json', 'utf-8');
//   const peopleArray = JSON.parse(peopleData);
//   const persons = peopleArray.filter(p => p.name.toLowerCase() === name.toLowerCase());
//   if (persons.length > 0) {
//       console.log('Persons found:', persons);
//   } else {
//       console.log('Person not found');
//   }
// }
// findPepoleByType('dana','name');

// findPersonByName('dana');

// 4. Search People by Age
// Same steps as “Search by Name”.
// Instead of name, search by age.
// behind the scenes you can use the same function as before, if you want.

//   async function findPersonByAge(age) {
//   const peopleData = await fs.readFile('./test-async/data/PEOPLE.json', 'utf-8');
//   const peopleArray = JSON.parse(peopleData);
//   const persons = peopleArray.filter(p => p.age === age);
//   if (persons.length > 0) {
//       console.log('Persons found:', persons);
//   } else {
//     console.log('Person not found');
//   }
// }
// findPersonByAge(34);

// findPepoleByType(34,'age');

// 5. Find Dangerous People
// Goal
// Find which people send the most dangerous messages. We do that by first processing the transcriptions and finding which age has the highest average danger score (calculated by processing all the content messages) - and then finding the people with the same age.
// Dangerous Calls
// A call in the transcriptions data is considered dangerous if the content of this transcription includes any of these words:
// death
// knife
// bomb
// attack
// Rules:
// Case does not matter (uppercase or lowercase).
// Each appearance of a dangerous word gives 1 point, including duplicates.
// Example:
// content: i hate to cut carrots with my knife, i want death, here is my knife
// Danger level: 3
// (2 times knife, 1 time death)
// suggested steps:
// Steps:
// Go through all call transcriptions.
// Calculate the danger level for each call’s content.
// Assign the danger level to the age written in the call transcription.
// For example: <age> : <array of danger levels, 1 per msg>
// {
// 	44: [12,34,4,1,3] // ,age 44 has 5 messages, with the scores 12…
// }
// you don’t have to save values if there is no danger score (i.e. = 0)
// Calculate the average danger level per age. Store this in a new object.
// Find the top 3 ages with the highest average danger level.
// From the people list, find all people whose age is one of these top 3 ages. Save it in a variable.
// send the list as a url param to general url + “/report”. Print the response.

// See appendix A at the end for some functions that might help!

async function getAllTranscriptions() {
  const peopleData = await fs.readFile(
    "./test-async/data/TRANSCRIPTIONS.json",
    "utf-8"
  );
  const transcriptionsArray = JSON.parse(peopleData);
  transcriptionsArray.forEach((transcription) => {
    transcription.dangerLevel = calculatedangerLevel(transcription.content);
  });
  return transcriptionsArray;
}
function calculatedangerLevel(content) {
  const dangerousWords = ["death", "knife", "bomb", "attack"];
  let dangerLevel = 0;
  const contentWords = content.toLowerCase().split(/\W+/);
  for (const word of contentWords) {
    if (dangerousWords.includes(word)) {
      dangerLevel++;
    }
  }
  return dangerLevel;
}

function calculateAverageDangerLevelPerAge(transcriptionsArray) {
  const dangerLevelsByAge = {};
  transcriptionsArray.forEach((transcription) => {
    if (transcription.dangerLevel > 0) {
      if (!dangerLevelsByAge[transcription.age]) {
        dangerLevelsByAge[transcription.age] = [];
      }
      dangerLevelsByAge[transcription.age].push(transcription.dangerLevel);
    }
  });
  console.log(dangerLevelsByAge)
  const averageDangerLevelByAge = {};
  for (const age in dangerLevelsByAge) {
    const dangerLevels = dangerLevelsByAge[age];
    const totalDangerLevel = dangerLevels.reduce(
      (acc, level) => acc + level,
      0
    );
    averageDangerLevelByAge[age] = totalDangerLevel / dangerLevels.length;
  }

  return averageDangerLevelByAge;
}
function arrAvgSortTop3(averageDangerLevelByAge) {
  const sortedAges = Object.entries(averageDangerLevelByAge)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 3);

  return sortedAges;
}

function peopleWithTop3Ages(top3Ages, peopleArray) {
  const arrPeopleDanger = [];
  const arrAges = top3Ages.map((age) => Number(age[0]));
  console.log(arrAges);
  peopleArray.forEach((person) => {
    if (arrAges.includes(person.age)) {
      arrPeopleDanger.push(person);
    }
  });
  return arrPeopleDanger;
}
const top3Ages = arrAvgSortTop3(
  calculateAverageDangerLevelPerAge(await getAllTranscriptions())
);

console.log(peopleWithTop3Ages(top3Ages, await getPeopleList()));
// console.log(await getAllTranscriptions())

import fs from "fs/promises";
const url = "https://spies-test-server.vercel.app/";

export async function getDataAndCreateJsonFile(data) {
  const response = await fetch(`${url}/${data}`);
  const callRecordsArray = await response.text();
  await fs.writeFile(
    `./data/${data.toUpperCase()}.json`,
    callRecordsArray
  );
  return callRecordsArray;
}

export async function findPepoleByType(data, type) {
  const peopleData = await fs.readFile(
    "./test-async/data/PEOPLE.json",
    "utf-8"
  );
  const peopleArray = JSON.parse(peopleData);
  let persons;
  if (type === "age") {
    persons = peopleArray.filter((p) => p[type] === data);
  } else {
    persons = peopleArray.filter(
      (p) => p[type].toLowerCase() === data.toLowerCase()
    );
  }

  if (persons.length > 0) {
    console.log("Persons found:", persons);
  } else {
    console.log("Person not found");
  }
}

const arr = [
  [4, 2, 2, 4],
  [1, 2, 3, 4],
  [5, 6, 7, 8],
];

function sumTeams(arr) {
  return arr.map((team) => {
    return team.reduce((acc, num) => acc + num, 0);
  });
}

console.log(sumTeams(arr));

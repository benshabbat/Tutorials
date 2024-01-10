// DICE ROLLER PROGRAM

function rollDices() {
  const numOfDices = document.getElementById("numOfDices").value;
  const dicesRes = document.getElementById("dicesRes");
  const dicesImg = document.getElementById("dicesImg");
  const dices = [];
  const images = [];

  for (let i = 0; i < numOfDices; i++) {
    const diceRandom = Math.floor(Math.random() * 6) + 1;
    dices.push(diceRandom);
    images.push(`<img src="images/dice${diceRandom}.png" alt="Dice ${diceRandom}">`);
  }
  dicesRes.textContent = dices;
  dicesImg.innerHTML = images.join('');
}

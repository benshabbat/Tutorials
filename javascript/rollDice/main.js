// DICE ROLLER PROGRAM

function rollDices() {
const numOfDices = document.getElementById("numOfDices").value;
const dicesRes = document.getElementById("dicesRes");
const dices=[];

    for(let i = 0; i < numOfDices; i++){
        const diceRandom = Math.floor(Math.random() * 6) + 1;
        dices.push(diceRandom);
        dicesRes.textContent = dices;
    }
}



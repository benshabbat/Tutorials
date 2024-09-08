// RANDOM NUMBER GENERATOR
const max = 4;
const min = 1;
document.getElementById("rollBtn").onclick = () => {
   //Random 1-6 numbers 
  document.getElementById("res").textContent =
    Math.floor(Math.random() * max) + min;
};

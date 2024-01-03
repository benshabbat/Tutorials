// RANDOM NUMBER GENERATOR
const max = 6;
const min = 1;
document.getElementById("rollBtn").onclick = () => {
  document.getElementById("res").textContent =
    Math.floor(Math.random() * max) + min;
};

let counter = 0;
document.getElementById("labelCounter").textContent = counter;

document.getElementById("decreaseBtn").onclick = () => {
  counter--;
  document.getElementById("labelCounter").textContent = counter;
};
document.getElementById("increaseBtn").onclick = () => {
  counter++;
  document.getElementById("labelCounter").textContent = counter;
};
document.getElementById("resetBtn").onclick = () => {
  counter = 0;
  document.getElementById("labelCounter").textContent = counter;
};

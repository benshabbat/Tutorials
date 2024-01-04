// .checked = property that determines the checked state of an
//                     HTML checkbox or radio button element

const subscribe = document.getElementById("subscribe");
const israel = document.getElementById("israel");
const brazil = document.getElementById("brazil");
const france = document.getElementById("france");

document.getElementById("submit").onclick = () => {
  subscribe.checked
    ? (document.getElementById("subres").textContent = "subscribed")
    : (document.getElementById("subres").textContent = "unsubscribed");
  israel.checked
    ? (document.getElementById("cityres").textContent = "israel")
    : brazil.checked
    ? (document.getElementById("cityres").textContent = "brazil")
    : france.checked
    ? (document.getElementById("cityres").textContent = "france")
    : "";
};

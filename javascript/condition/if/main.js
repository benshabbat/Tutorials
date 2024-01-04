// IF STATEMENTS = if a condition is true, execute some code
//                                   if not, do something else

const ageInput = document.getElementById("age");
const submit = document.getElementById("submit");
const res = document.getElementById("res");
let age;
submit.onclick = function () {
  age = ageInput.value;
  age = Number(age);
  if (age >= 100) {
    res.textContent = `You are TOO OLD to enter this site`;
  } else if (age == 0) {
    res.textContent = `You can't enter. You were just born.`;
  } else if (age >= 18) {
    res.textContent = `You are old enough to enter this site`;
  } else if (age < 0) {
    res.textContent = `Your age can't be below 0`;
  } else {
    res.textContent = `You must be 18+ to enter this site`;
  }
};

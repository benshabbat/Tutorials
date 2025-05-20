const form = document.getElementById("form");

const checkConfirmPassword = (password, confirmPassword) => {
  return password === confirmPassword;
};

const print = (firstName, email, password, confirmPassword) => {
  console.log(firstName);
  console.log(email);
  console.log(password);
  console.log(confirmPassword);
};

const checkEmail = (email) => {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailPattern.test(email);
};

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const firstName = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirmPassword").value;
  console.log("pass:" + checkConfirmPassword(password, confirmPassword));
  console.log("email" + checkEmail(email));
  print(firstName, email, password, confirmPassword);
});

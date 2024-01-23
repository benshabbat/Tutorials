const updateClock = () => {
  const clock = new Date();
  const hours = clock.getHours();
  const minutes = clock.getMinutes();
  const seconds = clock.getSeconds();
  document.getElementById("clock").textContent =
    hours + ":" + minutes + ":" + seconds;
};
updateClock();

const updateClock = () => {
  const clock = new Date();
  const hours = clock.getHours().toString.padStart(2, 0);
  const minutes = clock.getMinutes().toString.padStart(2, 0);
  const seconds = clock.getSeconds().toString.padStart(2, 0);
  const time = hours + ":" + minutes + ":" + seconds;
  //   hours = hours<10? "0"+hours:hours;
  //   minutes = minutes<10? "0"+minutes:minutes;
  //   seconds = seconds<10? "0"+seconds:seconds;
  document.getElementById("clock").textContent = time;
};
updateClock();
setInterval(updateClock, 1000);

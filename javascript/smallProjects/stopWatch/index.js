// STOPWATCH PROGRAM

const display = document.getElementById("display");
let timer = null;
let startTime = 0;
let elapsedTime = 0;
let isRunning = false;

function start(){
    if(!isRunning){
        startTime = Date.now() - elapsedTime;
        console.log(startTime,elapsedTime);
        timer = setInterval(update, 10);
        isRunning = true;
    }
}

function stop(){
    if(isRunning){
        clearInterval(timer);
        elapsedTime = Date.now() - startTime;
        console.log(elapsedTime,startTime);
        isRunning = false;
    }
}

function reset(){
    clearInterval(timer);
    startTime = 0;
    elapsedTime = 0;
    isRunning = false;    
    display.textContent = "00:00:00:00";
}

function update(){
    
    const currentTime = Date.now();
    elapsedTime = currentTime - startTime;

    let hours = Math.floor(elapsedTime / (1000 * 60 * 60)).toString().padStart(2, 0);
    let minutes = Math.floor(elapsedTime / (1000 * 60) % 60).toString().padStart(2, 0);
    let seconds = Math.floor(elapsedTime / 1000 % 60).toString().padStart(2, 0);
    let milliseconds = Math.floor(elapsedTime % 1000 / 10).toString().padStart(2, 0);
    const time = hours + ":" + minutes + ":" + seconds + ":" + milliseconds;
    display.textContent = time;

    //ex2

    // hours = String(hours).padStart(2, "0");
    // minutes = String(minutes).padStart(2, "0");
    // seconds = String(seconds).padStart(2, "0");
    // milliseconds = String(milliseconds).padStart(2, "0");

    // display.textContent = `${hours}:${minutes}:${seconds}:${milliseconds}`;
}
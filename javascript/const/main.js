
// const = a variable that can't be changed

const PI = 3.14159;
let radius;
let circumference;

// PI = 44;

document.getElementById("mySubmit").onclick = function(){
    radius = document.getElementById("radius").value;
    radius = Number(radius);
    circumference = 2 * PI * radius;
    document.getElementById("circumference").textContent = circumference + "cm";
}
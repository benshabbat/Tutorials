// setTimeout() = function in JavaScript that allows you to schedule
//                            the execution of a function after an amount of time 
//                            Times are approximate
//                            setTimeout(callback, delay);

// ---------- EXAMPLE 1 ----------
function hello() {
    window.alert("Hello");
}
 
setTimeout(hello, 3000);

// ---------- EXAMPLE 2 ----------
// clearTimeout() = can cancel a timeout before it triggers

const timeoutId = setTimeout(() => window.alert("Hello"), 3000);

clearTimeout(timeoutId);

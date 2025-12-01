
// Function Declaration
function nameFunction(){
    return "Alice";
}

// Function Expression
const ageFunction = function(){
    return 30;
};

// Arrow Function
const cityFunction = () => {
    return "New York";
};

// Annonymous Function
const countryFunction = function(){
    return "USA";
};


const arrFuncs = [nameFunction, ageFunction, cityFunction, countryFunction];


const decoratorFunction = (func)=>{
    function wrappedFunction(a,b){ 
    console.log("start function")
    const result = func(a,b);
    console.log(result);
    console.log("end function")
    return result;
    }
    return wrappedFunction;
}



const calculator = {
    add: (a, b) => a + b,
    
    subtract: (a, b) => a - b,
    
    multiply: (a, b) => a * b,
    
    divide: (a, b) => {
        if (b === 0) {
            return "Error: Division by zero";
        }
        return a / b;
    }
};

// const calc = calculator;
// const calcAdd = decoratorFunction(calc.add);
// const calcSubtract = decoratorFunction(calc.subtract);
// const calcMultiply = decoratorFunction(calc.multiply);
// const calcDivide = decoratorFunction(calc.divide);
// calcAdd(4,5)

const multiply =(num)=> num * 2;

const start = (fun , val) =>{
    console.log("Starting process...");
    return fun(val);
}
console.log(start(multiply, 5));
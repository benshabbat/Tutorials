// arithmetic operators = operands (values, variables, etc.)
//                                         operators (+ - * /)
//                                         ex. 11 = x + 5;

let num = 30;

console.log((num = num + 1));
console.log((num = num - 1));
console.log((num = num * 2));
console.log((num = num / 2));
console.log((num = num ** 2));

let num2 = num % 3;
console.log(num2);

console.log((num += 1));
console.log((num *= 2));
console.log((num /= 2));
console.log((num **= 2));
console.log((num %= 2));
console.log(num++);
console.log(num--);

/*
    operator precedence
    1. parenthesis ()
    2. exponents
    3. multiplication & division & modulo
    4. addition & subtraction
*/

console.log(5 + 4 - 6 * (6 + 4));

var input = require("fs").readFileSync("JavaScript/iniciante/stdin", 'utf8');

let value = input.split('\n');
let num1 = value.shift();
let num2 = value;

let prod  =  parseInt(num1) * parseInt(num2);

console.log(`PROD = ${prod}`)
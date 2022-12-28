var input = require("fs").readFileSync("JavaScript/iniciante/stdin", 'utf8');


let valores = input.split('\n');
let num1 = valores.shift()
let num2 = valores;
let soma = parseInt(num1) + parseInt(num2);

console.log(`X = ${soma}`)
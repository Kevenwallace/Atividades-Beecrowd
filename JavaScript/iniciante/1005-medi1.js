var input = require('fs').readFileSync('JavaScript/iniciante/stdin', 'utf8');

let value = input.split('\n');
let num1 = value.shift();
let num2 = value;

num1 = parseFloat(num1) * 3.5;
num2 = parseFloat(num2) * 7.5;

let soma = num1 + num2;
let media = soma / 11;
console.log(`MEDIA = ${media.toFixed(5)}`);

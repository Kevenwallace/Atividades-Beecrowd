var input = require("fs").readFileSync("JavaScript/iniciante/stdin", 'utf8');

const pi = 3.14159;

let area = (parseFloat(input)**2) * pi;
area = area.toFixed(4)
console.log(`A=${area}`);
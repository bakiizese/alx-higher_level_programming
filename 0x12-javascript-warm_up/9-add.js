#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (num1 && num2) {
  add(num1, num2);
} else {
  console.log('NaN');
}
function add (a, b) {
  console.log(a + b);
}

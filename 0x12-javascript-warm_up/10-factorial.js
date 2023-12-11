#!/usr/bin/node
const num = parseInt(process.argv[2], 10);

if (num) {
  console.log(factorial(num));
} else {
  console.log('1');
}

function factorial (num) {
  if (num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

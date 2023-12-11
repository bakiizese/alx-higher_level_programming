#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));

if (size) {
  for (let i = 1; i <= size; i++) {
    let sp = '';
    for (let j = 1; j <= size; j++) {
      sp += 'x';
    }
    console.log(sp);
  }
} else {
  console.log('Missing size');
}

#!/usr/bin/node
const size = parseInt(process.argv[2], 10);

if (size) {
  for (let i = 1; i <= size; i++) {
    for (let j = 1; j <= size; j++) {
      process.stdout.write('x');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}

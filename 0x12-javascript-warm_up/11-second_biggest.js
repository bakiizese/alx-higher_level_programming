#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log('0');
} else if (process.argv.length <= 3) {
  console.log('0');
} else {
  let max = process.argv[3];
  let maxs = max;
  for (let i = 2; i <= process.argv.length; i++) {
    if (max < process.argv[i]) {
      maxs = max;
      max = process.argv[i];
    }
  }
  console.log(maxs);
}

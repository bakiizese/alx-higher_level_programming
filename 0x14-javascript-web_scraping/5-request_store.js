#!/usr/bin/node

const request = require('request');
request(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const fs = require('fs');

  fs.writeFile(process.argv[3], body, 'utf8', err => {
    if (err) {
      console.log(err);
    }
  });
});

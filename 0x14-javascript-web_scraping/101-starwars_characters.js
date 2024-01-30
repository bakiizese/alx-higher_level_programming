#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  requr(characters, 0);
});

function requr (characters, idx) {
  request(characters[idx], function (err, resp, body) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(JSON.parse(body).name);
    if (idx + 1 < characters.length) {
      requr(characters, idx + 1);
    }
  });
}

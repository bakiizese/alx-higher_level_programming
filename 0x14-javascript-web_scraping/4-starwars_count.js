#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/people/18', (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.films.length);
});

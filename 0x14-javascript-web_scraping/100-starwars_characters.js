#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];

request.get(url + id, (err, resp, body) => {
  if (error) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  const datas = data.characters;

  for (const i of datas) {
    request.get(i, (err, resp, body1) => {
      if (err) {
        console.log(error);
        return;
      }
      const data2 = JSON.parse(body1);
      console.log(data2.name);
    });
  }
});

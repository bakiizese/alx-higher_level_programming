#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const urls = url.replace('films', 'people/18');
request(urls, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.films.length);
});

#!/usr/bin/node

const request = require('request');

request('https://jsonplaceholder.typicode.com/todos', (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  let data = JSON.parse(body);
  let count = 0;
  console.log(data[0].userId)
  for (; )
  {
    //console.log('---');
    //console.log(data[i]);
  }
});

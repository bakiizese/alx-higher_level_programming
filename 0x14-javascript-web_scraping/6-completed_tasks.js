#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const com = {};
  const tasks = JSON.parse(body);
  for (const i in tasks) {
    const task = tasks[i];
    if (task.completed === true) {
      if (com[task.userId] === undefined) {
        com[task.userId] = 1;
      } else {
        com[task.userId]++;
      }
    }
  }
  console.log(com);
});

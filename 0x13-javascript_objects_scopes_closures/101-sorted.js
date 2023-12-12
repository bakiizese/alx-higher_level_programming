#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newdic = {};
for (const key in dict) {
  const vl = dict[key];
  if (newdic[vl]) {
    newdic[vl].push(key);
  } else {
    newdic[vl] = [key];
  }
}
console.log(newdic);

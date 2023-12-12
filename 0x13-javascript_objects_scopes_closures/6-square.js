#!/usr/bin/node
const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let s = 'C';
    if (c === undefined) {
      s = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += s;
      }
      console.log(row);
    }
  }
}

module.exports = Square;

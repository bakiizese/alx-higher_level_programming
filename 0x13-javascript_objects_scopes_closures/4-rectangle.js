#!usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    const k = this.width;
    this.width = this.height;
    this.height = k;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'x';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;

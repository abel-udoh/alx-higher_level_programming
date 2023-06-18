#!/usr/bin/node
const SquareX = require('./5-square');

class Square extends SquareX {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let m = 0; m < this.height; m++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}

module.exports = Square;

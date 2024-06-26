#!/usr/bin/node
const Square = require('./5-square');

class Sqaure extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row = row + c;
        }
        console.log(row);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Sqaure;

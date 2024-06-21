#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Sqaure extends Rectangle {
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

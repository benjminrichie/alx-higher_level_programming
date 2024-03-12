#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let eye = 0; eye < this.height; eye++) {
      let s = '';
      for (let jhay = 0; jhay < this.width; jhay++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;

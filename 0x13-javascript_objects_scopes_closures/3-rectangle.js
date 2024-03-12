#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let eye = 0; eye < this.height; eye++) {
      let s = '';
      for (let jhay = 0; jhay < this.width; jhay++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;

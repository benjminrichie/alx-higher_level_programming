#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let eye = 0; eye < x; eye++) {
    theFunction();
  }
};

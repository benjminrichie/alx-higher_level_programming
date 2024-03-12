#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let eye = 0;
  while ((len - eye) > 0) {
    const aux = list[len];
    list[len] = list[eye];
    list[eye] = aux;
    eye++;
    len--;
  }
  return list;
};

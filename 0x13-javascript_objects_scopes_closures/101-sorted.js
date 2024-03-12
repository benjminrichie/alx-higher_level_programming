#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const jhay in valsUniq) {
  const list = [];
  for (const kay in totalist) {
    if (totalist[kay][1] === valsUniq[jhay]) {
      list.unshift(totalist[kay][0]);
    }
  }
  newDict[valsUniq[jhay]] = list;
}
console.log(newDict);

#!/usr/bin/node
function add (int1, int2) {
  const dResult = int1 + int2;
  console.log(dResult);
}

add(Number(process.argv[2]), Number(process.argv[3]));

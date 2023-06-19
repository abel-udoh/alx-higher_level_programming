#!/usr/bin/node
// a script that imports an array and computes a new array

const list = require('./100-data').list;

const anotherList = list.map(function (n, i) {
  return n * i;
});

console.log(list);
console.log(anotherList);

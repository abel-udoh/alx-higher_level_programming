#!/usr/bin/node
// a function that prints the number of arguments already printed

let arg = 0;
exports.logMe = function (item) {
  console.log(`${arg}: ${item}`);
  arg++;
};

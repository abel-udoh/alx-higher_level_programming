#!/usr/bin/node
exports.esrever = function (list) {
  const anotherList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    anotherList.push(list[i]);
  }
  return anotherList;
};

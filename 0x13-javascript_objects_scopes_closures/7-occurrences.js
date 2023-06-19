#!/usr/bin/node
// a function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let Occurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      Occurrences += 1;
    }
  }
  return Occurrences;
};

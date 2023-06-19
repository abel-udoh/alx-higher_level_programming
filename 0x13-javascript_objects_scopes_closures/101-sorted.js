#!/usr/bin/node

const dict = require('./101-data').dict;

const dict2 = {};
for (const j in dict) {
  if (dict[j] in dict2) {
    dict2[dict[j]].push(j);
  } else {
    dict2[dict[j]] = [j];
  }
}
console.log(dict2);

#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const mainList = process.argv.slice(2);
if (!mainList.sort((a, b) => b - a)[1]) {
  console.log(0);
} else {
  console.log(mainList.sort((a, b) => b - a)[1]);
}

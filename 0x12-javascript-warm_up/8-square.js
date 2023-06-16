#!/usr/bin/node
const times = parseInt(process.argv[2]);
let row = 0;
let column = 0;

if (isNaN(times)) {
  console.log('Missing size');
} else {
  for (row = 0; row < times; row++) {
    let result = '';
    for (column = 0; column < times; column++) {
      result += 'X';
    }
    console.log(result);
  }
}

#!/usr/bin/node
//print the first argument that is passed into it

if (process.argv[2] === undefined) {
  console.log('No Argument');
} else {
  console.log(process.argv[2]);
}

#!/usr/bin/node
//print a message according to the number of argument passed
if (process.argv.length === 2) {
console.log('No Argument');
} else if (process.argv.length === 3); {
console.log('Argument found');
} else {
console.log('Arguments found');
}

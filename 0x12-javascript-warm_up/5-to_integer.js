#!/usr/bin/node

const arg = process.argv.slice(2)[0];

if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(arg)}`);
}

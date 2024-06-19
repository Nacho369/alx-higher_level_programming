#!/usr/bin/node

const num = process.argv.slice(2)[0];

if (!isNaN(parseInt(num))) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}

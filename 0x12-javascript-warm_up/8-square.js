#!/usr/bin/node

const arg = Math.floor(Number(process.argv[2]));

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let square = '';
    for (let j = 0; j < arg; j++) {
      square += 'X';
    }
    console.log(square);
  }
}

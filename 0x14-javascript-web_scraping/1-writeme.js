#!/usr/bin/node
// A script that writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const writef = process.argv[3];

fs.writeFile(file, writef, 'UTF-8', function (error) {
  if (error) {
    console.log(error);
  }
});

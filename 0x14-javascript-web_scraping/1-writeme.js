#!/usr/bin/node
// A script that writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const write_f = process.argv[3];

fs.writeFile(file, write_f, 'UTF-8', function (error) {
  if (error) {
    console.log(error);
  }
});

#!/usr/bin/node
// A script that display the status code of a GET request

const args = process.argv[2];
let request = require('request');
request(args, function (error, response) {
  if (error) {
    console.log(error); // Print the error if one occurred
  } else console.log('code:', response && response.statusCode);
});

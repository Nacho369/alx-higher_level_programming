#!/usr/bin/node

const array = require('./100-data').list;

console.log(array);
let index = 0;
const nArray = array.map(function (x) {
  return (x * index++);
});
console.log(nArray);

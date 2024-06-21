#!/usr/bin/node

const { dict } = require('./101-data');
const nDict = {};
for (const N in dict) {
  if (nDict[dict[N]] === undefined) {
    nDict[dict[N]] = [];
  }
  nDict[dict[N]].push(N);
}
console.log(nDict);

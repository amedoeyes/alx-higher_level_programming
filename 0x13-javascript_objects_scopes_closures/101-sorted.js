#!/usr/bin/node

const newDict = Object.entries(require('./101-data').dict).reduce(
  (acc, [key, value]) => {
    if (!acc[value]) acc[value] = [];
    acc[value].push(key);
    return acc;
  },
  {}
);

console.log(newDict);

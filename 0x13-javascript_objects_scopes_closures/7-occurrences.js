#!/usr/bin/node

exports.nbOccurences = (list, searchElement) =>
  list.reduce((acc, cur) => (cur === searchElement ? acc + 1 : acc), 0);

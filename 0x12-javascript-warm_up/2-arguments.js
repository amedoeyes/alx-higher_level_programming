#!/usr/bin/node

const argc = process.argv.length - 2;
console.log(
  argc === 0 ? 'No argument' : `${argc === 1 ? 'Argument' : 'Arguments'} found`
);

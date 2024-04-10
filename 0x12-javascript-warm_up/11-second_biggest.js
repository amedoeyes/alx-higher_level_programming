#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
  process.exit(0);
}

console.log(args.sort((a, b) => b - a)[1]);

#!/usr/bin/node

const fs = require('fs').promises;

async function concat (file1, file2, dist) {
  const data1 = await fs.readFile(file1, 'utf8');
  const data2 = await fs.readFile(file2, 'utf8');
  await fs.writeFile(dist, data1 + data2);
}

const args = process.argv.slice(2);

concat(args[0], args[1], args[2]);

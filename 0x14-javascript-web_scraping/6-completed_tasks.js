#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const task of tasks) {
      if (task.completed) {
        if (completed[task.userId]) {
          completed[task.userId]++;
        } else {
          completed[task.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});

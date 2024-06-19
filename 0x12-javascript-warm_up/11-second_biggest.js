#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const list = [];
  for (let i = 2; i < process.argv.length; i++) {
    list.push(parseInt(process.argv[i]));
  }
  let max = list[0];
  let secoundmax = list[0];

  for (let j = 0; j < (process.argv.length - 3); j++) {
    if (list[j] > max) {
      max = list[j];
    }
  }
  for (let x = 0; x < (process.argv.length - 3); x++) {
    if (list[x] > secoundmax && list[x] < max) {
      secoundmax = list[x];
    }
  }
  console.log(secoundmax);
}

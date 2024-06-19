#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (process.argv[2] !== undefined) {
  if (isNaN(process.argv[2])) {
    console.log('Not a number');
  } else {
    console.log(parseInt(process.argv[2]));
  }
}

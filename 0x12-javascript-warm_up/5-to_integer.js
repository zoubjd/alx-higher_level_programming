#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (process.argv[2] !== undefined) {
  if (parseInt(process.argv[2])) {
      console.log(parseInt(process.argv[2]));
    } else {
        console.log('Not a number');
    }
}

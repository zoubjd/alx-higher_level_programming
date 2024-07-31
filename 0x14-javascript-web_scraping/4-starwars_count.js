#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonBody = JSON.parse(body);
    let count = 0;
    for (const result of jsonBody.results) {
      for (const charURL of result.characters) {
        if (charURL.includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

#!/usr/bin/node

const request = require('request');
id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = url + id;
request(fullUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonBody = JSON.parse(body);
    console.log(jsonBody.title);
  }
});

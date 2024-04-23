#!/usr/bin/node

/* a script that gets the contents of a webpage and stores it in a file. */

const request = require('request');
const fs = require('fs');
const my_url = process.argv[2];
const my_file = process.argv[3];

request(my_url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(my_file, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});

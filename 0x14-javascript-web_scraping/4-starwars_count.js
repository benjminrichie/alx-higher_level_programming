#!/usr/bin/node

// a script that prints the number of movies where
// the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let myCount = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          myCount += 1;
        }
      });
    });
    console.log(myCount);
  }
});

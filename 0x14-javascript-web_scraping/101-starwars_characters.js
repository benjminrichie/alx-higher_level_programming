#!/usr/bin/node

// a script that prints all characters of a Star Wars movie:

const request = require('request');

const movieId = process.argv[2];
const my_url = `https://swapi.dev/api/films/${movieId}/`;
let char = [];

request(my_url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  char = data.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === char.length) {
    return;
  }

  request(char[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getCharacters(index + 1);
  });
};

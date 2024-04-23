#!/usr/bin/node

// a script that prints all characters of
// a Star Wars movie:

const my_request = require('request');

const movieId = process.argv[2];
const my_url = `https://swapi.dev/api/films/${movieId}/`;

my_request.get(my_url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    my_request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});

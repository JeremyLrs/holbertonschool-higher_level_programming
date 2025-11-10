#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const char = document.querySelector('#character');

fetch(url).then((response) => {
  return response.json();
}).then((data) => {
  char.textContent = data.name;
});

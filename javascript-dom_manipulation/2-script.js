#!/usr/bin/node

const h = document.querySelector('header');
const red = document.querySelector('#red_header');

red.addEventListener('click', () => {
  h.classList.add('red');
});

#!/usr/bin/node

const h = document.querySelector('header');
const red = document.querySelector('#red_header');

red.style.cursor = 'pointer';

red.addEventListener('click', () => {
  h.style.color = '#FF0000';
});

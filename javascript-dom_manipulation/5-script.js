#!/usr/bin/node

const h = document.querySelector('header');
const update = document.querySelector('#update_header');

update.addEventListener('click', () => {
	header.textContent = 'New Header!!!'
});

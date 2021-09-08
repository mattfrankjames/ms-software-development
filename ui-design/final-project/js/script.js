const btn = document.querySelector('.nav__trigger');
const nav = document.querySelector('nav');
btn.addEventListener('click', () => {
  nav.classList.toggle('active');
});

const inputs = document.querySelectorAll('.inputField');
const labels = document.querySelectorAll('.inputLabel');

inputs.forEach((input) => {
  input.addEventListener('focus', () => {
    input.nextElementSibling.classList.add('active');
  });
});

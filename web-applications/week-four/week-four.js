// 1. window prompt for user name and password

function getUserNameAndPassword() {
  const username = prompt('Please enter a username.');
  const password = prompt('Please enter your password');
  return username, password;
}

// 2. Examples of objects and their usage

/* =============== The Date() object =============== */

const date = new Date();
// instantiates a new Date object
const now = date.now();
// captures this specific moment in time
const thisYear = date.getFullYear();
// captures this year
const todaysDate = date.getDate();
// captures

/*=============== the Math() object =============== */

const pi = Math.pi();
// captures the pi number
const minimum = Math.min(11, 5);
// captures the minimum of two values, in this case: 5
const maximum = Math.max(11, 5);
// captures the maximum of two values, in this case: 11

/* =============== the String() object =============== */

const myString = 'This is a string';

const allCaps = myString.toUpperCase();
// Because the myString variable is a string, we can use string methods on it like this that convert the string to all uppercase.
const s = myString.charAt(3);
// returns the character at the index passed to the charAt method (0 based)
const stingLength = myString.length;
// access the number of characters in a string

// 3. Events

/*============ the 'click' event ============ */

// grab an html element and listen for a click event, which triggers an alert

document.querySelector('button').addEventListener('click', function () {
  alert('You clicked a button!');
});

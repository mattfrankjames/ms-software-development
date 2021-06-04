// 1. An error first callback refers the first argument of a callback function being reserved for the error object and the second argument being reserved for sucessful response data.
// Example:

const fs = require('fs');

fs.readFile('/users.json', (err, data) => {
  if (err) {
    console.error(err);
    console.log('Unable to read file');
    return;
  }
  console.table(data);
});

// 2. Promises are akin to an IOU in Javascript. When an asynchronous request is made, a promise is returned that will either be resolved or rejected based on the results of the request. This allows the function to pause and wait for the results of the promise before moving on to the next bit of code.
// Example:
// Mark the function as async so as to use the `await` keyword in place of `.then()`
async function getData(data) {
  try {
    // fetch() returns a promise
    const response = await fetch(data);
    // await waits for the promise to resolve before executing the next line
    const formattedResponse = await response.json();
    return formattedResponse;
  } catch (error) {
    // Handle a rejected promise
    console.error(error);
  }
}
getData('https://api.github.com/mattfrankjames');

//3.  A test pyramid is a concept based around grouping automated testing in similar buckets. The pyramid is a way to vizualize the value different types of tests have for your application. For example, it's considered best to have a foundation of a large suite of unit tests that test functionality in isolation, a middle tier of integration tests that test how different components interact with each other, and a few end to end tests that test a full user flow.

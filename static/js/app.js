console.log("app.js loading..");

fetch('./get_question?level=easy')
  .then(
    function (response) {
      if (response.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }

      response.json().then(function (data) {
        console.log(data);
      });
    }
  )
  .catch(function (err) {
    console.log('Fetch Error', err);
  });

console.log("app.js loaded");
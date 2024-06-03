$(document).ready(function () {
  $.get(
    'https://hellosalut.stefanbohacek.dev/?lang=fr',
    (response, statusCode) => {
      $('#hello').text(response['hello']);
    },
  );
});

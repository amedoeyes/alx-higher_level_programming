$(document).ready(function () {
  $('input#btn_translate').on('click', () => {
    const langCode = $('input#language_code').val();
    const API_URL = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;
    $.get(API_URL, (reponse, statusCode) => {
      $('div#hello').text(reponse.hello);
    });
  });
});

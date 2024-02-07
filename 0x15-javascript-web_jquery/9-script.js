$.ajax({
  method: 'GET',
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  dataType: 'json'
}).done(function (data) {
  $.map(data, function (elm, i) {
    if (i == 'hello') {
      $('DIV#hello').text(elm);
    }
  });
});

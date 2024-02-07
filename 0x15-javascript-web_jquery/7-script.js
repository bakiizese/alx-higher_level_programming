$.ajax({
  method: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  dataType: 'json'
}).done(function (data) {
  $.map(data, function (elm, i) {
    if (i == 'name') {
      $('DIV#character').text(elm);
    }
  });
});

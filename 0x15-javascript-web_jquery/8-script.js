$.ajax({
  method: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  dataType: 'json'
}).done(function (data) {
  $.map(data, function (elm, i) {
    for (const j in elm) {
      const title_name = elm[j].title;
      $('UL#list_movies').append('<li>' + title_name + '</li>');
    }
  });
});

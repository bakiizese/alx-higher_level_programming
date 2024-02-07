$('document').ready(function () {
    function trans(){
        const url = 'https://hellosalut.stefanbohacek.dev/?';
        $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
            $('DIV#hello').html(data.hello);
        });
    }
    $('INPUT#btn_translate').click(trans);
    $('INPUT#language_code').keypress(function(event) {
        if (event.which === 13) {
          trans();
        }
    });
  });
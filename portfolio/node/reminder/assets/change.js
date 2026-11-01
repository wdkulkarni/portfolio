$(document).ready(function() {
    $('form').on('submit', function() {
        var date = $('#date');
        var name = $('#name');
        var listadd = {date: date.val(), name: name.val()};

        $.post('/', listadd, function(data, status) {
            location.reload();
        });

        return false;
    });

    $('li').click(function() {
        var item = $(this).text().replace(/ /g, '-');
        item = item.replace(/\//g, '-');
        $.get('/' + item, function(data, status) {
            location.reload();
        });
    });
});
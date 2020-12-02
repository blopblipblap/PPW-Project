$("#search").keyup(function() {
    var keyword = $("#search").val();
    //console.log(keyword);
    $.ajax({
        url: '/story8/data?q=' + keyword, 
        success: function(data){
            console.log(data);
            var array_books = data.items;
            $('.non-boldy').remove();
            for (i = 0; i < array_books.length; i++) {
                var html_desktop = "";
                var html_mobile = "";
                judul = array_books[i].volumeInfo.title;
                pengarang = array_books[i].volumeInfo.authors;
                html_desktop += '<tr class="non-boldy">';
                html_mobile += '<tr class="non-boldy">';
                html_desktop += '<td>' + (i+1) + '</td>';
                if (typeof array_books[i].volumeInfo.imageLinks === 'undefined') {
                    html_desktop += '<td><img class="cover" src="https://importstance.com/wp-content/uploads/2020/08/noavailable-3640.png"></td>';
                    html_mobile += '<td><img class="cover" src="https://importstance.com/wp-content/uploads/2020/08/noavailable-3640.png">';
                } else {
                    gambar = array_books[i].volumeInfo.imageLinks.smallThumbnail;
                    html_desktop += '<td><img class="cover" src=' + gambar + '></td>';
                    html_mobile += '<td><img class="cover" src=' + gambar + '>';
                }
                html_desktop += '<td>' + judul + '</td>';
                html_desktop += '<td>' + pengarang + '</td></tr>';
                html_mobile += '<br><br>';
                html_mobile += '<b>' + judul + '</b><br>';
                html_mobile += '<i>' + pengarang + '</i></td></tr>';
                
                $('.deskto > tbody:last-child').append(html_desktop);
                $('.mobil').append(html_mobile);
                console.log(judul);
            }
      }});
});
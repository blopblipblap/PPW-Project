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
                gambar = array_books[i].volumeInfo.imageLinks.smallThumbnail;
                judul = array_books[i].volumeInfo.title;
                pengarang = array_books[i].volumeInfo.authors;
                $('.deskto > tbody:last-child').append(
                    '<tr class="non-boldy"><td>' + (i+1) + '</td><td><img class="cover" src=' + gambar +
                    '></td><td>' + judul + 
                    '</td><td>' + pengarang + '</td></tr>');
                $('.mobil').append(
                    '<tr class="non-boldy"><td><img class="cover" src=' + gambar +
                    '><br><br><b>' + judul + '</b><br><i>' + pengarang + '</i></td></tr>');
                console.log(judul);
            }
      }});
});
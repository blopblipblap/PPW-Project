$("#search").keyup(function() {
    var keyword = $("#search").val();
    //console.log(keyword);
    $.ajax({
        url: "https://www.googleapis.com/books/v1/volumes?q=" + keyword, 
        success: function(result){
            var array_books = result.items;
            //console.log(array_books);
            $('.non-boldy').remove();
            for (i = 0; i < array_books.length; i++) {
                gambar = array_books[i].volumeInfo.imageLinks.smallThumbnail;
                judul = array_books[i].volumeInfo.title;
                pengarang = array_books[i].volumeInfo.authors;
                $('.tabel > tbody:last-child').append(
                    '<tr class="non-boldy"><td>' + (i+1) + '</td><td><img class="cover" src=' + gambar +
                    '></td><td>' + judul + 
                    '</td><td>' + pengarang + '</td></tr>')
                console.log(judul);
            }
      }});
});
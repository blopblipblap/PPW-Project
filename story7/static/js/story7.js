$(function () {
    $("#accordion").accordion({ 
        heightStyle: 'content', 
        header: "> div > div",
        active: false,
        collapsible: true
     });
});

$(document).ready(function () {
    var accordionlist = $("#accordion");
    var length = $(accordionlist).children().length;
    var atasJalan = false;
    var bawahJalan = false;

    $(".atas").click(function (e) {
        e.stopPropagation();
        e.preventDefault();
        var selected = $(this).parent().parent().parent();
        var selectedIdx = selected.index()
        if (selectedIdx > 0) {    
            atasJalan = true;
            jQuery($(accordionlist).children().eq(selectedIdx - 1)).before(jQuery($(accordionlist).children().eq(selectedIdx)));
            selectedIdx = selectedIdx - 1;
        }
    });

    $(".bawah").click(function (e) {
        e.stopPropagation();
        e.preventDefault();
        var selected = $(this).parent().parent().parent();
        var selectedIdx = selected.index()
        if (selectedIdx < length) {
            bawahJalan = true;
            jQuery($(accordionlist).children().eq(selectedIdx + 1)).after(jQuery($(accordionlist).children().eq(selectedIdx)));
            selectedIdx = selectedIdx + 1;
        }
    });
});


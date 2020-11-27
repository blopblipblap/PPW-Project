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

    $(".atas").click(function (e) {
        e.preventDefault();
        var selected = $(this).parent().parent().parent();
        var selectedIdx = selected.index()
        if (selectedIdx > 0) {
            jQuery($(accordionlist).children().eq(selectedIdx - 1)).before(jQuery($(accordionlist).children().eq(selectedIdx)));
            selectedIdx = selectedIdx - 1;
        }
    });

    $(".bawah").click(function (e) {
        e.preventDefault();
        var selected = $(this).parent().parent().parent();
        var selectedIdx = selected.index()
        if (selectedIdx < length) {
            jQuery($(accordionlist).children().eq(selectedIdx + 1)).after(jQuery($(accordionlist).children().eq(selectedIdx)));
            selectedIdx = selectedIdx + 1;
        }
    });
});


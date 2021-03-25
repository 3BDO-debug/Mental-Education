function make_button_active(tab) {
    //Get item siblings
    var siblings = tab.siblings();

    /* Remove active class on all buttons
    siblings.each(function(){
        $(this).removeClass('active');
    }) */

    //Add the clicked button class
    tab.addClass('watched');
}

//Attach events to highlight-watched
$(document).ready(function () {

    if (localStorage) {
        var ind = localStorage['tab']
        make_button_active($('.highlight-watched li').eq(ind));
    }

    $(".highlight-watched li").click(function () {
        if (localStorage) {
            localStorage['tab'] = $(this).index();
        }
        make_button_active($(this));
    });

});
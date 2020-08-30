$(document).ready(function(){ 
    $('.buttonBad').click(function() { 
        $(this).toggleClass('activeBad');
    });
});

$(document).ready(function(){ 
    $('.buttonGood').click(function() { 
        $(this).toggleClass('activeGood');
        var scroll = $(window).scrollTop();
        // yada
        $("html").scrollTop(scroll);
    });
});


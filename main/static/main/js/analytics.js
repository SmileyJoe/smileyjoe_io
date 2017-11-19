window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
ga('create', GA_TRACKING_ID, 'auto');

if(GA_PAGE) {
    ga('send', 'pageview', GA_PAGE);
} else {
    ga('send', 'pageview');
}

$(window).bind( 'hashchange', function(e) {
    var hash = window.location.hash.substr(1);

    if(hash) {
        hash = "#" + hash;
    }

    var pageName = GA_PAGE + hash;
    ga('send', 'pageview', pageName);
});

function ga_link(category, title){
    ga('send', 'event', category, 'link', title);
}
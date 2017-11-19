$(document).ready(function() {
    var span = $('<span class="input_text centered">')
        .appendTo('body')
        .css('visibility','hidden');
    var textarea = $('.expand_input');

    span.text(textarea.text())
        .width(textarea.width())
        .css('font', textarea.css('font'));

    textarea.on({
        input: function () {
            var text = $(this).val();
            span.text(text);
            $(this).height(text ? span.height() : '1.1em');
        },
        keypress: function (e) {
            if (e.which == 13){
                $('.form_secret').submit();
                return false;
            }
        },

    });
});
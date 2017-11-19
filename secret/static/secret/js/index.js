$(document).ready(function() {
    var span = $('<span class="input_text centered">')
        .appendTo('body')
        .css('visibility','hidden');
    var textarea = $('.expand_input');
    var textCount = $('.count');

    span.text(textarea.text())
        .width(textarea.width())
        .css('font', textarea.css('font'));

    textarea.on({
        input: function () {
            var text = $(this).val();
            span.text(text);
            $(this).height(text ? span.height() : '1.1em');
            textCount.text(text.length + '/' + textCount.text().split('/')[1]);
        },
        keypress: function (e) {
            if (e.which == 13){
                $('.form_secret').submit();
                return false;
            }
        },

    });
});
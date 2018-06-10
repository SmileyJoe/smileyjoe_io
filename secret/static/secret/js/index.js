$(document).ready(function() {
    // Adapted from https://stackoverflow.com/a/23819536 //

    // Creates a span that will have the same text as the input //
    // this will then increase in size, so we can set the input //
    // height based on it //
    var span = $('<span class="input_text centered">')
        .appendTo('body')
        .css('visibility','hidden');
    var textarea = $('.expand_input');
    var textCount = $('.count');

    // give the span the same properties as the input //
    span.text(textarea.text())
        .width(textarea.width())
        .css('font', textarea.css('font'));

    textarea.on({
        // this fires off when text is entered //
        input: function () {
            var text = $(this).val();
            span.text(text);
            $(this).height(span.height());
            textCount.text(text.length + '/' + textCount.text().split('/')[1]);
        },
        keypress: function (e) {
            // code 13 is the enter key, we want to submit the form instead //
            // of the default new line //
            if (e.which == 13){
                $('.form_secret').submit();
                return false;
            }
        }
    });
});
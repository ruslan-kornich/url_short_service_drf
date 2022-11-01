$(function () {
    var el;
    $("#rng").change(function () {
        el = $(this);
        el
            .next("#ong")
            .text(el.val());
    })
        .trigger('change');
});
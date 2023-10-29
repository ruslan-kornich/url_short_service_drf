$(function () {
    var el;
    $("#rng").on('input', function () {
        el = $(this);
        var dayCount = el.val();
        $("#ong").text(dayCount + (dayCount === "1" ? " day" : " days"));
    }).trigger('input'); // Инициализация значения при загрузке страницы
});

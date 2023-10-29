$(document).on('submit', '#post-form', function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/create',
        data: {
            link: $('#link').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            rng: $('input[name=rng]').val(),
        },
        success: function (data) {
            $('#short-url-display').html(data);

            // Показываем иконку для копирования, когда короткая ссылка была сгенерирована
            $('#copy-icon').removeClass('d-none');
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const copyIcon = document.getElementById("copy-icon");
    const shortUrlDisplay = document.getElementById("short-url-display");
    const copyToastEl = document.getElementById("copy-toast");
    const copyToast = new bootstrap.Toast(copyToastEl);

    copyIcon.addEventListener("click", function() {
        if (shortUrlDisplay.innerText !== "") {
            // Copying the short URL
            const textarea = document.createElement('textarea');
            textarea.value = shortUrlDisplay.innerText;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);

            // Showing the toast notification
            copyToast.show();
        }
    });
});

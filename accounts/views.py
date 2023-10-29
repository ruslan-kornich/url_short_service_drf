from django.shortcuts import redirect


def custom_logout(request):
    # Выход пользователя
    from django.contrib.auth import logout
    logout(request)
    # После выхода выполните редирект на главную страницу
    return redirect('index')

from django.shortcuts import redirect


def custom_logout(request):
    from django.contrib.auth import logout

    logout(request)

    return redirect("index")

from django.conf import settings
from django.contrib.auth import login as django_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from config import settings


def sign_up(request):
    #     username = request.POST.get('username')
    #     password1 = request.POST.get('password1')
    #     password2 = request.POST.get('password2')
    #
    #
    #     print('username', username)
    #     print('password1', password1)
    #     print('password2', password2)

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    context = {"form": form}

    return render(request, "registration/signup.html", context)


def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())
        from django.urls import reverse

        next = request.GET.get("next")
        if next:
            return redirect(next)

        return redirect(reverse("blog:list"))
    else:
        form = AuthenticationForm(request)

    context = {"form": form}
    return render(request, "registration/login.html", context)

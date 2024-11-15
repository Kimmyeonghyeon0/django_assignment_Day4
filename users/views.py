from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as django_login

from django.shortcuts import render, get_object_or_404
from .models import Todo


def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        from django.shortcuts import redirect

        return redirect(settings.LOGIN_URL)

    context = {
        "form": form,
    }
    return render(request, "registration/signup.html", context)


def login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())
        return redirect(settings.LOGIN_REDIRECT_URL)

    context = {
        "form": form,
    }
    return render(request, "registration/login.html", context)


#
# def todo_list(request):
#     todos = Todo.objects.all()
#     return render(request, 'todo_list.html', {'todos': todos})
#
# def todo_info(request, todo_id):
#     todo = get_object_or_404(Todo, id=todo_id)
#     return render(request, 'todo_info.html', {'todo': todo})

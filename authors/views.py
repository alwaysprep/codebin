from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from .forms import AuthorForm, UserForm
# Create your views here.


def register(request):

    if request.method == "POST":

        user_form = UserForm(request.POST)
        author_form = AuthorForm(request.POST, request.FILES)

        if author_form.is_valid() and user_form.is_valid():
            user = user_form.save()

            author = author_form.save(commit=False)
            author.user = user
            author.save()

            return redirect("login")

        else:
            return render(request, 'authors/register.html', {'author_form': author_form,
                                                            'user_form': user_form})

    elif request.method == "GET":

        author_form = AuthorForm()
        user_form = UserForm()

        return render(request, 'authors/register.html', {'author_form': author_form,
                                                         'user_form': user_form})


def author_login(request):

    if request.method == "GET":
        return render(request, "authors/login.html")

    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("create_gist")
        else:
            return redirect("index")


def author_logout(request):
    logout(request)
    return redirect("index")

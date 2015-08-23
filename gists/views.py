from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import GistForm
from gists.models import Gist
from snippets.forms import SnippetForm
from snippets.models import Snippet
# Create your views here.


def user_exists(request):
    return bool(request.user.username)


def home(request):
    if user_exists(request):
        return redirect("create_gist")
    return render(request, "index.html", {})



def generate_snippet_and_gist_forms(request):
    # Gist UpdateForm or CreateForm
    possible_gist = Gist.objects.filter(title=request.POST.get("title", None), author=request.user.author)
    if possible_gist.exists():
        gist_form = GistForm(data=request.POST, instance=possible_gist.first())
    else:
        gist_form = GistForm(data=request.POST)

    # Snippet UpdateForm or CreateForm
    snippet_form = SnippetForm(data=request.POST)
    if possible_gist.exists():
        possible_snippet = Snippet.objects.filter(file_name=request.POST.get("file_name", None), gist=possible_gist.first())
        if possible_snippet.exists():
            snippet_form = SnippetForm(data=request.POST, instance=possible_snippet.first())

    return snippet_form, gist_form


def create(request, gi=None, snip=None):

    if request.method == "POST":

        if not user_exists(request):
            return HttpResponse("You Have No Right To Modify This Gist")

        snippet_form, gist_form = generate_snippet_and_gist_forms(request)

        if gist_form.is_valid() and snippet_form.is_valid():

            gist = gist_form.save(commit=False)
            gist.author = request.user.author
            gist.save()

            snippet = snippet_form.save(commit=False)
            snippet.gist = gist
            snippet.save()

            return redirect("create_gist", gi=gist.slug, snip=snippet.slug)

        # Not Valid Form
        else:
            gists = Gist.objects.filter(author=request.user.author)

            if gists.exists():
                snippets = gists.first().snippets.all()
                snippet = snippets.first()
                gist = gists.get(title=request.POST.get("title", None))
                return render(request, "gists/create.html", {"gists": gists, "snippets": snippets, "snippet": snippet, "gist": gist, "gist_form": gist_form, "snippet_form": snippet_form})
            else:
                return render(request, "gists/create.html", {"gists": gists, "gist_form": gist_form, "snippet_form": snippet_form})

    elif request.method == "GET":
        # Not Logged In

        if not request.user.username:
            if not gi or not snip:
                return HttpResponse("please specify gist and sippet")

            try:
                gists = Gist.objects.filter(isPrivate=False)
                snippets = gists.get(slug=gi).snippets.all()
                snippet = snippets.get(slug=snip)
                gist = gists.get(slug=gi)
            except ObjectDoesNotExist:
                return HttpResponse("You dont have rigts to see this file")

            return render(request, "gists/create.html", {"gists": gists,  "snippets": snippets, "snippet": snippet, "gist": gist})

        ## Logged In
        gists = Gist.objects.filter(author=request.user.author)
        if not gists.exists():
            return render(request, "gists/create.html", {})

        if snip:
            snippets = gists.get(slug=gi).snippets.all()
            snippet = snippets.get(slug=snip)
            gist = gists.get(slug=gi, author=request.user.author)
        elif gi:
            snippets = gists.get(slug=gi).snippets.all()
            snippet = snippets.first()
            gist = gists.get(slug=gi, author=request.user.author)
        else:
            snippets = gists.first().snippets.all()
            snippet = snippets.first()
            gist = gists.first()

        return render(request, "gists/create.html", {"gists": gists,  "snippets": snippets, "snippet": snippet, "gist": gist})




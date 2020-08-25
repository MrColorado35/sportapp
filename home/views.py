from django.shortcuts import render


def index(request):
    """A view that will return a home page """

    return render(request, "home/index.html")

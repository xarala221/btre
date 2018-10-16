from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "pages/index.html", context)

def about(request):
    context = {}
    return render(request, "pages/about.html", context)

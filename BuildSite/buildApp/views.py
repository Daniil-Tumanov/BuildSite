from django.shortcuts import render


def index(request):
    return render(request, 'buildApp/index.html')


def about(request):
    return render(request, 'buildApp/about.html')

from django.shortcuts import render


def index(request):
    return render(request, 'commons/index.html', {})

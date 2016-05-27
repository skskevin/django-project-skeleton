from django.shortcuts import render


def index(request):
    return render(request, 'manager/example/index.html')

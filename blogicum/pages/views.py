from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def about(request):
    template = 'about.html'
    return render(request, template)


def rules(request, id):
    template = 'rules.html'
    return render(request, template)
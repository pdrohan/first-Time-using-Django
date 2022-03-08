from django.shortcuts import render
from django.http import HttpResponse
from .forms import Digitform


def Test(request):
    return render(request, 'results.html')


# Create your views here.
def Home(request):
    template_name = 'testnig.html'
    return render(request, template_name)

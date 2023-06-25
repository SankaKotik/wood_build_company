from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def redirect_view(request):
    response = redirect('/main/')
    return response

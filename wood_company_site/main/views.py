from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from services.models import Service


# Create your views here.
def index(request):
    cards = Service.objects.all()
    return render(request, 'main/index.html', {'data': cards})


def redirect_view(request):
    response = redirect('/main/')
    return response

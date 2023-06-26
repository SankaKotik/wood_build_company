from django.shortcuts import render

from .models import Service


# Create your views here.
def index(request):
    cards = Service.objects.all()
    return render(request, 'services/usl.html', {'data': cards})
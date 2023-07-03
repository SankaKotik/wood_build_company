from django.http import JsonResponse
from django.shortcuts import render

from .models import Service


# Create your views here.
# def index(request):
#     cards = Service.objects.all()[:3]
#     total_obj = Service.objects.count()
#     print(len(cards))
#     return render(request, 'services/usl.html', {'data': cards, 'total_obj': total_obj})


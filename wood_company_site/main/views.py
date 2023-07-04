from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

from services.models import Service

from main.models import PortfolioCard


# Create your views here.
def index(request):
    cards = Service.objects.all()[:4]
    total_obj = Service.objects.count()
    portfolio_cards = PortfolioCard.objects.all()
    return render(request, 'main/index.html', {'data': cards, 'total_obj': total_obj, 'portfolio': portfolio_cards})

def load_more(request):
    offset = request.GET.get('offset')
    offset_int = int(offset)
    limit = 4
    # post_obj = Post.objects.all()[offset_int:offset_int+limit]
    services = list(Service.objects.values()[offset_int:offset_int+limit])
    colors = ['blue', 'red', 'green', 'yellow']
    for i, service in enumerate(services):
        service['color'] = colors[i]
    data = {
        'data': services
    }
    return JsonResponse(data=data)

def redirect_view(request):
    response = redirect('/main/')
    return response

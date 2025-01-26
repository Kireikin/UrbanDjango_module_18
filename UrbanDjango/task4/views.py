from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Cart4(TemplateView):
    template_name = 'fourth_task/cart.html'


def shop4(request):
    context = {'game1': "Atomic Heart",
               'game2':"Cyberpunk 2077",
               'game3': "PayDay2"
               }
    return render(request, 'fourth_task/games.html', context)


def func_platform4(request):
    return render(request, 'fourth_task/platform.html')

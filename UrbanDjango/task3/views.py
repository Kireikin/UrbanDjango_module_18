from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Cart(TemplateView):
    template_name = 'third_task/cart.html'


class Shop(TemplateView):
    template_name = 'third_task/games.html'


def func_platform(request):
    return render(request, 'third_task/platform.html')

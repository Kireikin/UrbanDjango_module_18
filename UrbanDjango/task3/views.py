from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Cart3(TemplateView):
    template_name = 'third_task/cart.html'


class Shop3(TemplateView):
    template_name = 'third_task/games.html'


def func_platform3(request):
    return render(request, 'third_task/platform.html')

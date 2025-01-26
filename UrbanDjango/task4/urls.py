from django.contrib import admin
from django.urls import path
from . import views
from .views import func_platform4, Cart4, shop4
from django.views.generic import TemplateView


app_name = 'task4'

urlpatterns = [
    # post view
    path('admin/', admin.site.urls),
    path('cart4/', Cart4.as_view()),
    path('shop4/', shop4),
    path('', func_platform4),
]

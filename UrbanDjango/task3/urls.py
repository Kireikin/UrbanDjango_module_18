from django.contrib import admin
from django.urls import path
from . import views
from .views import func_platform, Cart, Shop
from django.views.generic import TemplateView


app_name = 'task3'

urlpatterns = [
    # post view
    path('admin/', admin.site.urls),
    path('cart/', Cart.as_view()),
    path('games/', Shop.as_view()),
    path('', func_platform),
]

from django.contrib import admin
from django.urls import path
from . import views
from .views import func_platform3, Cart3, Shop3
from django.views.generic import TemplateView


app_name = 'task3'

urlpatterns = [
    # post view
    path('admin/', admin.site.urls),
    path('cart3/', Cart3.as_view()),
    path('games3/', Shop3.as_view()),
    path('', func_platform3),
]

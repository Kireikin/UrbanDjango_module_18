from django.contrib import admin
from django.urls import path
from .views import sign_up_by_django, sign_up_by_html, choose  # index


app_name = 'task5'

urlpatterns = [
    # post view
    path('admin/', admin.site.urls),
    path('', choose),
    path('django/', sign_up_by_django),
    path('html/', sign_up_by_html),
]

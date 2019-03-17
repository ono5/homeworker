from django.urls import path

from .views import kakeibo_page

app_name = 'kakeibo'

urlpatterns = [
    path('', kakeibo_page, name='input'),
]

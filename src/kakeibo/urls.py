from django.urls import path

from .views import kakeibo_page, kakeibo_list

app_name = 'kakeibo'

urlpatterns = [
    path('', kakeibo_page, name='input'),
    path('list/', kakeibo_list, name='show'),
]

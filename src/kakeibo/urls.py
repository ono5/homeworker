from django.urls import path

from .views import kakeibo_page


urlpatterns = [
    path('', kakeibo_page, name='kakeibo'),
]

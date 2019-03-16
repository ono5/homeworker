from django.http import HttpResponse
from django.shortcuts import render


def kakeibo_page(request):
    return render(request, 'kakeibo/kakeibo.html')

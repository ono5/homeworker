from django.contrib import messages
from django.shortcuts import render
from .forms import KakeiboInputForm


def kakeibo_page(request):
    if request.method == 'POST':
        user = request.user

        form = KakeiboInputForm(request.POST)
        if form.is_valid():
            form.save(user)
            messages.success(request, 'Input Credit', 'successfully')
            form = KakeiboInputForm()
        else:
            messages.error(request, 'Error input credit')
    else:
        form = KakeiboInputForm()
    data = {
        'form': form
    }
    return render(request, 'kakeibo/kakeibo.html', data)

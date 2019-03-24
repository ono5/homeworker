from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse

from .forms import KakeiboInputForm
from .models import Payment

@login_required
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


@login_required
def kakeibo_list(request):
    payment_list = list(Payment.objects.all().filter(user=request.user.id))
    data_list = []
    for payment in payment_list:
        data_list.append(payment.item)
    print("payment_list = ", payment_list)

    data = {
        'data_list': data_list
    }
    return render(request, 'kakeibo/kakeibo_list.html', data)

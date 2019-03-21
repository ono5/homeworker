from django import forms

from .params import *
from .models import Category, Payment


class KakeiboInputForm(forms.ModelForm):

    def save(self, for_kakeibo):
        self.instance.user = for_kakeibo
        return super().save()

    class Meta:
        model = Payment
        fields = ('category', 'credit', 'item')
        exclude = ('created_at', 'updated_at')
        widgets = {
            'category': forms.fields.Select( attrs={
                'class': 'custom-select'
            } ),
            'credit': forms.fields.TextInput(attrs={
                'placeholder': CREDIT,
                'class': 'form-control input-lg'
            }),
            'item': forms.fields.TextInput(attrs={
                'placeholder': ITEM,
                'class': 'form-control input-lg'
            })
        }

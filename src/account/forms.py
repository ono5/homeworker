from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

from .params import *


class CustomLoginForm(AuthenticationForm):
    """Lgin Form"""

    username = forms.CharField(widget=forms.TextInput( attrs={'placeholder': USERNAME}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput( attrs={'placeholder': PASSWORD}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'auth-box'


class CustomPasswordResetForm(PasswordResetForm):
    """Password Reset Form"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'auth-box'
            field.widget.attrs['placeholder'] = EMAIL


class UserRegistrationForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': USERNAME}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': FIRSTNAME}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': EMAIL}))
    password = forms.CharField(label=PASSWORD, widget=forms.PasswordInput(attrs={'placeholder': PASSWORD}))
    password2 = forms.CharField(label=CONFIRM_PASSWORD, widget=forms.PasswordInput(attrs={'placeholder': CONFIRM_PASSWORD}))

    class Meta:
        model = User
        # if the user chooses a username that already exists, they will get a validation error
        fields = ('username', 'first_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'

    def clean_password2(self):
        """
        Custom validation
        you can provide a clean_<fieldname>() method to amy of your form fields in order to clean the value
        or raise form validation errors for a specific field.
        """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']

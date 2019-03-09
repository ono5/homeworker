from django import forms


class LoginForm(forms.Form):
    """Authenticate users against the database"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

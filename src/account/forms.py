from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    """Lgin Form"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'auth-box'


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        # if the user chooses a username that already exists, they will get a validation error
        fields = ('username', 'first_name', 'email')

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
